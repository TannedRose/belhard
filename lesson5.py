# a = 0
# if a:
#     print("a ровно нулю")
# else:
#     print("a НЕ РОВНО 0")
# a = 5

# is_even = "no" if a % 2 else "yeah"

# if a % 2:
#     is_even = "no"
# else:
#     is_even = "yeah"

# print(isinstance(False, int)) # =True(bool=int) дочерний тип

# city = None
# user = {}
# user["city"] = city and "Mogilev"
# print(user)
#
# text = "Hello world"
#
# for i in numbers:
#     print(i ** 2)
# for i in enumerate(text):
#     print(i)
# e = range(2, 10 ,2)
# for i in range(10):
#     if i == 10:
#         break
#     print(i)
# else:
#     print("Finish!")

# i = 0
# while i < 10:
#     i += 1
#     print(i)

# a = input("Введите число ")
# while not a.isdigit():
#     a = input("Введите число ")

# data = {"key1": "value1", "key2": "value2"}
# objs = ["AB", "CD2", "EF34"]
# for i, j, *k in objs:
#     print(i, j, k)

# words = ["Hello", "Python", "world"]
# for word in words:
#     for letter in word:
#         print(letter)

# for _ in range(5): #best
#     print("Hello")

# i = 5
# for i in range(10):
#     print("Hello")
# print(i)

# a = input("введите строку ")
# b = [i.upper() for i in a if i.isalpha()]
# for i in a:
#     if i.isalpha():
#         b.append(i.upper())
#     print(i)

# numbers = [4, -2, 3, -5, 6, 7, 8, -10, 12, 13]
# result = [number for number in numbers if number <0 ]
# print(result)

# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except ValueError:
#     print("Not number")
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print("not exception")
# finally:
#     print("always")
# status_codes = {
#     200: "OK",
#     201: "CREATED",
#     202: "ACCEPTED"
# }
# status = 200
# if status == 200:
#     print("OK")
# elif status == 201:
#     print("CREATED")
# elif status == 202:
#     print("ACCEPTED")
# else:
#     print("error")

color = (255, 0, 0)
match color:
    case (r, g, b):
        print("RGB")
        print(r, g, b)
    case _:
        print("invalid")