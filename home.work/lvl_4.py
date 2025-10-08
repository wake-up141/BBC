from math import *

class Calculator:
    def __init__(self, sign: str):
        self.num1 = num1
        self.num2 = num2
        self.result = 0
        self.sign = sign

    def calculate(self):
        if self.sign == '+':
            self.result = self.num1 + self.num2
        elif self.sign == '-':
            self.result = self.num1 - self.num2
        elif self.sign == '*':
            self.result = self.num1 * self.num2
        elif self.sign == '/':
            self.result = self.num1 / self.num2
        return self.result

    def pro(self):
        if self.sign == 'sin':
            self.result = sin(self.num1)
        elif self.sign == 'cos':
            self.result = cos(self.num1)
        return self.result

sign = str(input('Введите знак операции: '))
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
mycalc = Calculator(sign)


if sign in ['+', '-', '*', '/']:
    print(mycalc.calculate())
else:
    print(mycalc.pro())
