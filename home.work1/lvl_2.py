def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    return a / b


num1 = float(input("Введите первое число: "))
op = input("Введите знак операции (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if op == "+":
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif op == "-":
    print(f"{num1} - {num2} = {sub(num1, num2)}")
elif op == "*":
    print(f"{num1} * {num2} = {mul(num1, num2)}")
elif op == "/":
    print(f"{num1} / {num2} = {div(num1, num2)}")
else:
    print("Неизвестная операция")
