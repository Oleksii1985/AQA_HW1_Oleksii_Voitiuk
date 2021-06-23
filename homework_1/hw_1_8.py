"""
8. Создайте 2 переменные john, marta. Переменные должны быть словарями с ключами: full_name, age, salary, gender,
friends, coordinates.
Требования к структуре:
Full_name - полное имя
Age - возраст
Salary - заработная плата
Gender - пол человека (используйте булев тип)
Friends - список друзей из задачи 6
Coordinates - долгота и широта из задачи 7
Вывести в консоль джона и марту ключ и значение: “key => value” где key это ключ пары из словаря а value
это значение пары из словаря.
"""
john = {
    "full_name": "John Jonson",
    "age": 22,
    "salary": 5.5,
    "gender": True,
    "friends": ["Luk", "Bob", "Sam", "Lisa"],
    "coordinates": (46.4625565, 30.74601465),
}
for key, value in john.items():
    print(key)
    print(value)

marta = {
    "full_name": "Marta Jonson",
    "age": 20,
    "salary": 5.1,
    "gender": False,
    "friends": ["Lucy", "Melany", "Samantha", "Ray"],
    "coordinates": (46.4625565, 30.74601465),
}
for key, value in marta.items():
    print(key)
    print(value)

# Good. But output should be like:
# for key, value in marta.items():
#     print(f"{key} => {value}")
