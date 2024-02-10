# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
data = {
    1: {"name": "mike", "surname": 'kozlov', "fnumber": '+375291111111', "email": 'mikeK@gmail.com'},
    2: {"name": "liz", "surname": 'ivanova', "fnumber": '+375441111111', "email": None},
    3: {"name": "ivan", "surname": 'melnikov', "fnumber": '+375292222222', "email": ""},
    4: {"name": "kate", "surname": 'elkina', "fnumber": '+375442222222', "email": 'EKate@gmail.com'}
}
for j in data.items():
    if "email" not in j:
        for i in data:
            if not data[i]["email"]:
                print(data[i]["name"], end=' ')

