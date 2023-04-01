
def process_string():
    s = input("Введите произвольную строку: ")
    # Выводим длину строки
    print(f"Длина строки: {len(s)}")

    # Проходим по символам
    for i, c in enumerate(s):
        # Пропускаем третий символ
        if i == 2:
            continue
        # Проверяем на символ "c"
        elif c == 'c':
            print("Строка содержит символ 'c'")
        # Выводим символ
        else:
            print(c, end='')

    # Переводим строку
    print()


if __name__ == '__main__':
    process_string()
