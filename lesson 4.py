# objs = [1,2,3,4, "hello", "world", True, None]
# text = "hello world"
# a = list(text)
# print(a)

# objs[0:2] = "First"
# print(objs)

# zeros = [i+2 for i in range(100)]
# print(zeros)
# text = "hello"
# objs = [2, 4, 6 ,8, 6, 10, 6, text]
# objs2 = objs[1:3]
# objs.remove(6)
# del objs[1:3]
# # del objs[1:3]
# print(objs)

# a = objs.pop(5)
# print(objs)
# print(a)

# a = []
# a.append(a)
# print(getrefcount(a))

a = [1, 2, 3, 4]
# a.append(5)
# a.insert(0,0)
# print(a)

# a.extend([5, 6, 7,])
# a += [5, 6, 7]
# print(a)
# b = a+a
# print(b)

# a = [3, 4, 3, 5, 5,]
# print(a.count(3))

# a = [4, 5, 3 ,2, -34, 23 ,4]
# a.sort(key=abs)
# print(a)

# a = [1, 2, 3, 4, 5]
# b = a[::-1]
# a.reverse()
# print(b)

# a = [1, 2, 3, 4]
# b = a[:]
# c = a.copy()
# b.append(5)
# print(a)

# b = (1, 2, 3, 4, [], 5, 6, 7,)
# a.append("World")
# b[4].append("Hello")
# print(b)

# a = {3, 4, 3, 4, 3, 4, 3, }
# print(a)

# a = set("Hello")
# print(a)

# a = {1, 2, 3}
# b = {6, 7, 8}
# print(a.issubset(b))
# print(a <= b)
# print(a == b)
# c = a.union(b, [0, 8, 1, ], ("Hello", "World"))
# print(a | b | {5, 6, 5, 3})
# print(a.difference(b))
# print(a.intersection(b))

# a = frozenset([1, 2, 3, 4, 5])
# print(a)

# a = {}
# print(type(a))
# data ={
#     "first_name": "Alex",
#     "age": 34,
#     "is_human": True,
#     "languages": ["ru", "en"],
# }
# data["first_name"] = "Max"

# data = dict([("name", "Alex"), ("age", 34), ("lang", [])])
# print(data)
# data = dict.fromkeys(["name", "age", "city"], "H/Y")
# data["is_human"] = "Minsk"
# print(data)

# data ={
#     "first_name": "Alex",
#     "age": 34,
#     "is_human": True,
#     "languages": ["ru", "en"],
# }
# print(data.setdefault("city", "Minsk"))
# print(data)
# del data["is_human"]
# print(data.pop("is_human"))
# print(data)
# print(list(data.keys()))
# print(data.values())
# print(data.items())
# data2 = {"first_nname": "Max", "city": "Minsk"}
# data3 = data | data2
# print(data3)

# a, b, c =(1, 2, 3)
# print(a)
# print(b)
# print(c)

words = ["Hello", "World", "Hello", "Python"]
c = Counter(words)
c.substract
print(c)
