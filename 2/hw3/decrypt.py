import sys


def decrypt(encryption: str) -> str:
    """
    Расшифровывает строку по правилам Васи.

    Параметры:
        encryption (str): зашифрованная строка.

    Возвращает:
        str: расшифрованная строка.
    """
    result = []          # стек для накопления расшифрованных символов
    i = 0
    n = len(encryption)

    while i < n:
        ch = encryption[i]
        if ch != '.':
            # Обычный символ – добавляем в результат
            result.append(ch)
            i += 1
        else:
            # Текущий символ – точка, проверяем следующую
            if i + 1 < n and encryption[i + 1] == '.':
                # Две точки подряд – удаляем последний символ из результата
                if result:
                    result.pop()
                i += 2
            else:
                # Одиночная точка – просто пропускаем
                i += 1

    return ''.join(result)


if __name__ == '__main__':
    # Читаем весь стандартный ввод и удаляем завершающий перевод строки
    data = sys.stdin.read().rstrip('\n')
    decryption = decrypt(data)
    print(decryption)
