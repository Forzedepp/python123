import sys


def get_mean_size(ls_output: str) -> float:
    """
    Вычисляет средний размер обычных файлов в выводе команды ls -l.

    Параметры:
        ls_output (str): многострочный вывод команды ls -l.

    Возвращает:
        float: средний размер в байтах. Если файлов нет, возвращает 0.0.
    """
    lines = ls_output.strip().splitlines()
    if not lines:
        return 0.0

    # Пропускаем строку "total ...", если она есть
    # В некоторых системах первой строкой может быть "total N", но не всегда.
    # Просто проверим, что строка начинается с "total", и пропустим её.
    start_index = 0
    if lines and lines[0].startswith('total'):
        start_index = 1

    sizes = []
    for line in lines[start_index:]:
        # Пропускаем пустые строки
        if not line.strip():
            continue
        columns = line.split()
        # Проверяем, что это обычный файл (первый символ '-')
        if len(columns) >= 5 and columns[0].startswith('-'):
            try:
                size = int(columns[4])  # размер — пятый столбец
                sizes.append(size)
            except ValueError:
                # Если не удалось преобразовать, пропускаем
                continue

    if not sizes:
        return 0.0

    total = sum(sizes)
    return total / len(sizes)


if __name__ == '__main__':
    # Читаем весь входной поток (стандартный ввод)
    data = sys.stdin.read()
    mean_size = get_mean_size(data)
    print(mean_size)
