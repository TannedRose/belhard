# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3
number1 = input("введите первое число ")
number2 = input("введите второе число ")
number3 = input("введите третье число ")
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
answer = (number1 + number2 + number3) / 3
print(round(answer, 3))