import random
import math


def add(*numbers):
    return sum(numbers)


def subtract(first, *numbers):
    return first - sum(numbers)


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def divide(first, *numbers):
    result = first
    for number in numbers:
        result /= number
    return result


def power(first, second):
    return first ** second


def absolute(number):
    return abs(number)


def random_number(minimum, maximum):
    return random.randint(minimum, maximum)


def factorial(number):
    return math.factorial(number)


def arccos(number):
    return math.acos(number)


def calculator():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': power,
        'abs': absolute,
        'rand': random_number,
        '!': factorial,
        'arccos': arccos
    }
    operation = input("Введите операцию (+, -, /, *, **, abs, rand, !, arccos): ")
    if operation not in operations:
        print("Некорректная операция")
        return
    try:
        if operation in ['+', '-', '/', '*', '**']:
            numbers = [float(input(f"Введите число {i + 1}: ")) for i in range(2)]
            result = operations[operation](*numbers)
        elif operation in ['abs', '!']:
            number = float(input("Введите число: "))
            result = operations[operation](number)
        elif operation == 'rand':
            minimum, maximum = [int(input(f"Введите {parameter}: ")) for parameter in
                                ['минимальное число', 'максимальное число']]
            result = operations[operation](minimum, maximum)
        elif operation == 'arccos':
            number = float(input("Введите число: "))
            result = operations[operation](number)
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка ввода")


if __name__ == '__main__':
    calculator()
