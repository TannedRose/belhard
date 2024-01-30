# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
number1 = input("введите первое число ")
number2 = input("введите второе число ")
number3 = input("введите третье число ")
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
first = (number1 <0)
second = (number2 <0)
third = (number3 <0)
first = int(first)
second = int(second)
third = int(third)
answer = first + second + third
answer = int(answer)
answer2 = 3 - answer
print(f"количество отрицательных {answer}")
print(f"количество положительных {answer2}")
