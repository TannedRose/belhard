# class User:
#     def __init__(self, first_name: str, email: str) -> None:
#         self.first_name = first_name.title()
#         self.email = email.lower()
#
#     def __str__(self) -> str:
#         return f"User first_name={self.first_name}, email={self.email}"
#
#
# class Manager(User):
#     def work(self):
#         print("work...")
#
# vasya = Manager(first_name="vasya", email="vasya@gmail.com")
# print(vasya)
# vasya.work()
# print(Manager.mro())
#
# class A:
#
#     def __init__(self, name: str):
#         self.name = name
#
#
#
#     def foo(self):
#         return self.name.upper()
#
#
# class B(A):
#
#     def foo (self):
#         result = super().foo()
#         return result * 2

# class User:
#     def __init__(self, first_name: str, last_name: str,):
#         self.first_name = first_name
#         self.last_name = last_name
#
#         @property
#         def full_name(self) -> str:
#             return f"{self.first_name} {self.last_name}"
#         @full_name.setter
#         def full_name(self, value:str):
#             self.first_name = value.split()[0]
#             self.last_name = value.split()[1]
#
# vasya = User(first_name="vasya", last_name="pypkin")

# class User:
#     __slots__ = ("name", "email")
#
#     def __init__(self, name:str, email: str) -> None:
#         self.name = name
#         self.email = email
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def email(self):
#         return self.__email

# from dataclasses import dataclass
#
# @dataclass(frozen=True)
# class User:
#     name: str
#     email: str


from abc import ABC, abstractmethod

# class AbstractView(ABC):
#
#
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass
#     @classmethod
#     def dispatch(cls, request):
#         pass
#
# class AbstractPhone(ABC):
#
# class Mobilephone(AbstractPhone)
#
#     @abstractmethod
#     def sms(self):
#         pass
#     @abstractmethod
#     def call(self):
#         pass
#
#
#
# class StaticPhone(AbstractPhone):
#     def sms(self):
#         pass
#     def call(self):
#         pass

# модуль верхнгего уровня не доолжен зависить от модуля нижнего уровняб оба должны зависеть от абстракции
# обстракция не должна зависеть от деталейб а детали должны зависеть отобстракции

# class YandexM:
#
#     def getmusic(self, name):
#         print("LOGICA")
#
# class Music:
#
#     def __init__(self, music: YandexM):
#         self.music = music
#
#     def get(self, name):
#         print("LOGICA")
#         self.music.getmusic(name=name)
#
# class Engine:
#
#     def __init__(self, volume, type_):
#         self.volume = volume
#         self.type = type_
#
# class Car:
#
#     def __init__(self, marka, engine_volume, engine_type):
#         self.marka = marka
#         self.engine = Engine("2000", "GAS")
# engine = Engine(volume="2500", type_="GAS")
# car = Car(marka="Bowarskoe Musornoe Wedro")
# mercedes = Car(marka="Mercedes", engine=engine)

