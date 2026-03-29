import os
import logging
import sys
import unittest

from redirect import Redirect


# Настройка конфигурации логгирования
logging.basicConfig(level=logging.DEBUG)

# текущая дирректория для файлов:
cur_dir = os.path.dirname(__file__)


class TestRedirect(unittest.TestCase):

    def setUp(self):
        """Сохраняем оригинальные значения потоков."""
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        # путь к файлам:
        self.stdout_path = os.path.join(cur_dir, 'stdout.txt')
        self.stderr_path = os.path.join(cur_dir, 'stderr.txt')

    def test_redirect_stdout(self):
        with open(self.stdout_path, 'a') as f_out:
            with Redirect(stdout=f_out):
                print('Это стандартный поток вывода')
                # проверяем, что sys.stdout был перенаправлен:
                self.assertNotEqual(sys.stdout, self.original_stdout)
                # logging.debug(
                #     f'\nCurrent stdout: {sys.stdout}\n'
                #     f'Original stdout: {self.original_stdout}'
                # )
        # выход из контекст-менеджера,
        # проверяем что sys.stdout восстановлен:
        self.assertEqual(sys.stdout, self.original_stdout)
        # logging.debug(
        #     f'\nstdout: {sys.stdout}\n'
        #     f'Original stdout: {self.original_stdout}'
        # )
    
    def test_redirect_stderr(self):
        with open(self.stderr_path, 'a') as f_err:
            with Redirect(stderr=f_err):
                try: 
                    raise Exception('Это стандартный поток ошибок')
                except Exception:
                    # Записываем трассировку стека в stderr:
                    import traceback
                    traceback.print_exc(file=sys.stderr)
                    # проверяем, что sys.stderr был перенаправлен:
                    self.assertNotEqual(sys.stderr, self.original_stderr)
                    # logging.debug(
                    #     f'\nCurrent stderr: {sys.stderr}\n'
                    #     f'Original stderr: {self.original_stderr}'
                    # )
        # выход из контекст-менеджера,
        # проверяем что sys.stderr восстановлен:
        self.assertEqual(sys.stderr, self.original_stderr)
        # logging.debug(
        #     f'\nstderr: {sys.stderr}\n'
        #     f'Original stderr: {self.original_stderr}'
        # )

    def test_redirect(self):
        with open(os.path.join(cur_dir, 'stdout.txt'), 'a') as f_out,\
             open(os.path.join(cur_dir, 'stderr.txt'), 'a') as f_err:
            with Redirect(stdout=f_out, stderr=f_err):
                print('Второй стандартный поток вывода')
                try:
                    raise Exception('Второй стандартный поток ошибок')
                except Exception:
                    import traceback
                    traceback.print_exc(file=sys.stderr)

                    self.assertNotEqual(sys.stdout, self.original_stdout)
                    self.assertNotEqual(sys.stderr, self.original_stderr)

        self.assertEqual(sys.stdout, self.original_stdout)
        self.assertEqual(sys.stderr, self.original_stderr)

    def test_no_args(self):
        with Redirect():
            self.assertEqual(sys.stdout, self.original_stdout)
            self.assertEqual(sys.stderr, self.original_stderr)
        self.assertEqual(sys.stdout, self.original_stdout)
        self.assertEqual(sys.stderr, self.original_stderr)
        

if __name__ == '__main__':
    unittest.main()
    # with open(os.path.join(cur_dir,'test_results.txt'), 'a') as test_file_stream:
    #     runner = unittest.TextTestRunner(stream=test_file_stream)
    #     unittest.main(testRunner=runner)
