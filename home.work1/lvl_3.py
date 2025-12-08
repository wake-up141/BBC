def calc(num1: int, num2: int, sign: str):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        return num1 / num2
    elif sign == '**':
        return num1 ** num2
    return 'Ошибка ввода'

num1 = int(input('Введите первое число: '))
sign = str(input('Введите знак операции: '))
num2 = int(input('Введите второе число: '))

print(calc(num1, num2, sign))
