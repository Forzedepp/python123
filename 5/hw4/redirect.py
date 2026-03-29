"""
Иногда возникает необходимость перенаправить вывод в нужное 
нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта 
(например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""


import sys

from types import TracebackType
from typing import Type, Literal, IO


class Redirect:
    """
    контекстный менеджер Redirect,
    перенаправляет stdout и stderr в указанные IO-объекты
    """
    def __init__(self, stdout: IO = None, stderr: IO = None) -> None:
        self.stdout = stdout
        self.stderr = stderr
        self._original_stdout = None
        self._original_stderr = None

    def __enter__(self):
        if self.stdout:
            # сохраняем текущие значения:
            self._original_stdout = sys.stdout
            # устанавливаем новые:
            sys.stdout = self.stdout
        if self.stderr:
            # сохраняем текущие значения:
            self._original_stderr = sys.stderr
            # устанавливаем новые:
            sys.stderr = self.stderr

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        if self.stdout:
            # восстанавливаем исходные значения:
            sys.stdout = self._original_stdout
        if self.stderr:
            # восстанавливаем исходные значения:
            sys.stderr = self._original_stderr
