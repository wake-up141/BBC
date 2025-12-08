num1 = float(input("Введите первое число: "))
op = input("Введите знак операции (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Неизвестная операция")
