# Вывести четные числа от 2 до N по 5 в строку
n = int(input("введите верхнюю границу "))
for i in range(2, n, 2):
    if i % 5 == 0:
        print(i)
    else:
        print(i, end=",")





