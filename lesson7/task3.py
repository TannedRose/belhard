# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError
new_name = str(input("введите новое имя "))
class Category(object):
    categories: list[str] = []

    @classmethod
    def add(cls, category: str) -> int:
        category = category.title()
        if category is not cls.categories:
            cls.categories.append(category)
            return cls.categories.index(category)
        raise ValueError(f"category: {category}")

    @classmethod
    def delete(cls,pk: int) -> None:
        try:
            del cls.categories[pk]
        except IndexError:
            ...

    @classmethod
    def update(cls,pk:int, category:str) -> None:
        category = category.title()
        try:
            old_category = cls.get(pk=pk)
        except IndexError







