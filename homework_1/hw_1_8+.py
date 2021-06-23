"""
Задача со звездочкой:
Задача с пункта 8. Вместо строк в списке друзей должны быть такие же словари как джон и марта.
Создайте по 2 друга для джона и марты. Выведите в консоль поля Джона и Марты.
"""
luk = {
    "full_name": "Luk Jonson",
    "age": 20,
    "salary": 5.8,
    "gender": True,
    "friends": ["Luk", "Bob", "Sam", "Lisa"],
    "coordinates": (46.4625565, 30.74601465),
}
lisa = {
    "full_name": "Lisa Jonson",
    "age": 20,
    "salary": 5.1,
    "gender": False,
    "friends": ["Lucy", "Melany", "Samantha", "Ray"],
    "coordinates": (46.4625565, 30.74601465),
}
john = {
    "full_name": "John Jonson",
    "age": 22,
    "salary": 5.5,
    "gender": True,
    "friends": [luk, lisa],
    "coordinates": (46.4625565, 30.74601465),
}
for key, value in john.items():
    print(key)
    print(value)

lucy = {
    "full_name": "Lucy Jonson",
    "age": 25,
    "salary": 5.8,
    "gender": False,
    "friends": ["Lucy", "Melany", "Samantha", "Ray"],
    "coordinates": (46.4625565, 30.74601465),
}
bob = {
    "full_name": "Bob Jonson",
    "age": 22,
    "salary": 6.2,
    "gender": True,
    "friends": ["Luk", "Bob", "Sam", "Lisa"],
    "coordinates": (46.4625565, 30.74601465),
}
marta = {
    "full_name": "Marta Jonson",
    "age": 20,
    "salary": 5.1,
    "gender": False,
    "friends": [lucy, bob],
    "coordinates": (46.4625565, 30.74601465),
}
for key, value in marta.items():
    print(key)
    print(value)
