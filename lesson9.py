# file = open(file=".output.txt", mode="w", encoding="utf-8-sig")
# print(file.writable())
# file.write("Hello World\n")
# file.writelines(["Python\n", "Pycharm\n"])
# print(file.read())
# print(file)
# print(file.readline())
# file.seek(0)
# for line in file:
#     print(line)
# file.close()
# with open(file=".output.txt", mode="w", encoding="utf-8-sig") as file:
#     print(file.closed)
# print(file.closed)


# class DataBase(object):
#
#     def __init__(self):
#         self.is_close = True
#
#     def close(self):
#         self.is_close = False
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is ValueError:
#             return True
#         self.close()
#
#
# with DataBase() as session:  # type: DataBase
#     print(session.is_close)
#     raise ValueError
# print(session.is_close)
# try:
from json import loads, load, dumps, dump
# except ImportError:
#     from json import load, loads, dumps, dump


# with open(file="./input.json", mode="rt", encoding="utf-8") as file:
#     data = load(file)
#     print(data)


# data = {
#     "id": 1,
#     "name": "Coffee",
#     "price": 5.5
# }
# with open(file="./output.json", mode="wt", encoding="utf-8") as file:
#     text = dumps(data)
#     print(text)
    # dump(data, file, indent=2, ensure_ascii=False)

# from yaml import safe_load
#
# with open("./config.yml", "rt", encoding="'utf-8") as file:
#     data = safe_load(file)
#     print(data)
from csv import reader, writer, DictReader, DictWriter

# with open("./input.csv", "rt", encoding="utf-8") as file:
# data = [{
#         "id": 1,
#         "name": "Coffee"
#     },
#     {
#         "id": 2,
#         "name": "Pancake"
#     }
#     ]

from pydantic import BaseModel, EmailStr


# class UserRegion(BaseModel):
#     first_name: str
#     last_name: str = field(default=None)
#     age: str
#     email: str
#     lang: list[int]
#
# data = UserRegion.parse_file(path="./user_register.json")
# print(data)
# class Produt(BaseModel):
    
