# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

fnumber = int(input("введите первое число "))
action = input("введите знак ")
snumber = int(input("введите второе число "))
if action == "+":
    print(fnumber + snumber)
elif action == "-":
    print(fnumber - snumber)
elif action == "/":
    print(fnumber / snumber)
elif action == "*":
    print(fnumber * snumber)
else:
    print("невозможно выполнить действие(неверный оператор) ")
