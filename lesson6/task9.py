# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
data = {
        1: {"name": "mike", "surname": 'kozlov', "fnumber": '+375291111111', "email": 'mikeK@gmail.com'},
        2: {"name": "liz", "surname": 'ivanova', "fnumber": '+375441111111', "email": ' '},
        3: {"name": "ivan", "surname": 'melnikov', "fnumber": '+375292222222', "email": ""},
        4: {"name": "ivan2", "surname": 'melnikov', "fnumber": '+375293333333'},
        5: {"name": "ivan3", "surname": 'melnikov', "fnumber": '+375294444444', "email": 'ugouvu'}
       }

for user_id, info_user in data.items():
    if 'email' not in info_user or ('@' and '.' not in info_user['email']):
            print(info_user['name'])





