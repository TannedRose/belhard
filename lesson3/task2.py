# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3
number1 = int(input("введите первое число "))
number2 = int(input("введите второе число "))
number3 = int(input("введите третье число "))

answer = (number1 + number2 + number3) / 3
print(round(answer, 3))