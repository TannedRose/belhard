# class User:
#     tablename = "user"
#
#     @classmethod
#     def change_tablename(cls, new_tablename):
#         cls.tablename = new_tablename
#
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#     def __init__(self, name, email, password, age):
#         self.name = name
#         self.password = password
#         self.email = email
#         self.is_active = False
#         self.age = age
#         # self.i = -1
#
#     def __iter__(self):
#         return self
#
#     def __len__(self):
#         return len(self.password)
#     def info(self):
#         return f"name={self.name} email={self.email} password={self.password}"
#     def __lt__(self, other):
#         if isinstance(other, User):
#             return self.age < other.age
#         elif isinstance(other, (int, float)):
#             return self.age < other
#         raise TypeError(f"'<' not supported between istance of 'User' and '{type(other)}")
#
#     def __bool__(self):
#         return self.is_active
#     def __int__(self):
#         return self.age
#     def set_name(self, new_name: str):
#         self.name = new_name
#
#
# user1 = User(name="vasya", email="vasya2gmail.com", password="Qwerty1!", age=10)
# user2 = User(name="petya", email="petya@gmail.com", password="VeryStrongPassword1!", age=11)
# # user1.set_name(new_name="max")
# print(user1.info())
# print(user2.info())
# print(int(user1))
#
# product = {
#     "title": "Laptop",
#     "description": "Powerful!",
#     "price": 1500
#
# }
# def change_product_price(product, percent):
#     product["price"] = product["price"] * (1 + percent)
#
# change_product_price(product=product, percent=0.05)
# print(product)
#
# print(print.__doc__)
#
#
# def multiply(a: int, b: int) -> int:
#     """произведение 2х целых чисел
#
#     :param a: первый множитель
#     :type a: int
#     :param a: второй множитель
#     :type a: int
#     :return: результат произвведения
#     :rtype: int
#     :raise TupeError: если один из мнодителей не число
#     """
#
#     return a * b
