# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

# a = ['hello', 1,  '2', 3, 'world']
# print(type(a))

a = ["test", 1, False, "2", [2]]

# print([i for i in a if isinstance(i, str)])
for i in a:
    if isinstance(i, str):
        print(i, end=', ')

