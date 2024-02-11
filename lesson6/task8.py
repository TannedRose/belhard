# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
a = {
    'France': 'paris',
    'belarus': 'minsk',
    'germany': 'berlin',
    'poland': 'warsaw',
    'russia': 'moscow',
    'albania': 'tirana',
    'austria': 'vienna',
    'belgium': 'brussels',
    'united kingdom': 'london',
    'ukraine': 'kiev'
}
b = input('введите столицу европейской страны ')
for i in a:
    if a[i] == b:
        print(i)

