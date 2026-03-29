import os
from typing import Union

def get_summary_rss(ps_output_file_path: str) -> str:
    """
    Вычисляет суммарный объём потребляемой памяти (RSS) из вывода команды ps aux.
    
    Параметры:
        ps_output_file_path (str): путь к файлу с выводом ps aux.
    
    Возвращает:
        str: суммарный RSS в человекочитаемом формате (например, "123.45 MiB").
    """
    total_rss_bytes = 0

    with open(ps_output_file_path, 'r') as f:
        lines = f.readlines()[1:]  # пропускаем строку заголовка

    for line in lines:
        columns = line.split()
        if len(columns) < 6:
            continue  # если строка повреждена, пропускаем
        try:
            rss = int(columns[5])  # RSS — шестой столбец (индекс 5)
            total_rss_bytes += rss
        except ValueError:
            continue  # если не число, пропускаем

    # Перевод в человекочитаемый формат
    units = ["Б", "KiB", "MiB", "GiB", "TiB"]
    size = float(total_rss_bytes)
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1

    return f"{size:.2f} {units[unit_index]}"


if __name__ == '__main__':
    path: str = 'output_file.txt'  # укажите ваш путь к файлу
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
