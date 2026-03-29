""" Тест для задачи 2 - Дешифратор """


import unittest

from Module_03.homework.hw2.decrypt import decrypt


class TestDecrypt(unittest.TestCase):

    # отдельные функции____________________________________________________:
    def test_one_dot(self):
        encrypted_text = 'абра-кадабра.'
        expected_decrypted_text = 'абра-кадабра'
        self.assertEqual(decrypt(encrypted_text), expected_decrypted_text)

    def test_two_dots(self):
        encrypted_text = 'абраа..-кадабра'
        expected_decrypted_text = 'абра-кадабра'
        self.assertEqual(decrypt(encrypted_text), expected_decrypted_text)


    # контекст-менеджер subTest___________________________________________:
    def test_decrypt(self):
        encrypted_texts = [
            ('абра-кадабра.', 'абра-кадабра'),
            ('абраа..-кадабра', 'абра-кадабра'),
            (' абраа..-.кадабра', ' абра-кадабра'),
            ('абра--..кадабра', 'абра-кадабра'),
            ('абрау...-кадабра', 'абра-кадабра'),
            # сделаем ошибку:
            ('абра-кадабра', ''),
            ('абр......a.', 'a'),
            ('1..2.3', '23'), 
            ('.', ''),
            ('1.......................', '')
        ]
        for encrypted_text, expected_text in encrypted_texts:
            with self.subTest(encrypted_text=encrypted_text):
                decrypted_text = decrypt(encrypted_text)
                self.assertEqual(decrypted_text, expected_text)

"""
В начале определяется список encrypted_texts, 
который содержит пары зашифрованных текстов и ожидаемых расшифрованных текстов.
Каждая пара представлена в виде кортежа внутри списка.

Далее используется цикл for, чтобы итерироваться по списку encrypted_texts.

На каждой итерации переменные encrypted_text и expected_text 
принимают значения из текущего кортежа.

Внутри цикла for создается контекстный менеджер subTest, 
который позволяет запускать тесты для каждой пары значений 
и в случае неудачи точно указывать, для какой пары значений тест не прошел.

Внутри контекста subTest вызывается функция decrypt 
с зашифрованным текстом encrypted_text, а затем сравнивается результат 
с ожидаемым расшифрованным текстом expected_decrypted_text 
с помощью self.assertEqual.

Если какой-либо тест не проходит 
(например, результат вызова decrypt не соответствует ожидаемому результату), 
выводится подробное сообщение об ошибке, указывающее на то, 
какой именно тест не прошел.
"""
