"""
1. Создать переменные john_salary и marta_salary вещественного типа (с плавающей точкой).
Присвоить созданным переменным значения по своему усмотрению. Вывести в консоль методом print значения обеих переменных.
"""
john_salary = 5.2
marta_salary = 4.9
print(f"John's salary is: {john_salary}$ per hour")
print(f"Marta's salary is: {marta_salary}$ per hour")

"""
2. Создать переменные john_age и marta_age целочисленного типа. 
Присвоить созданным переменным значения по своему усмотрению. Вывести в консоль методом print значения обеих переменных.
"""
john_age = 20
marta_age = 19
print(f"John's age is: {john_age} years old")
print(f"Marta's age is: {marta_age} years old")

"""
3. Создать переменные john_name и marta_name строкового типа. 
Присвоить созданным переменным значения по своему усмотрению. Вывести в консоль методом print значения обеих переменных.
"""
john_name = "John"
marta_name = "Marta"
print(f"John's name is: {john_name}")
print(f"Marta's name is: {marta_name}")

"""
4. Создать переменные john_gender и marta_gender булевого типа. 
Пусть john будет принимать истинное значение а marta ложное. Вывести в консоль методом print значения обеих переменных.
"""
john_gender = True
marta_gender = False
print(john_gender)
print(marta_gender)

"""
5. Создать переменные john_friends и marta_friends. Присвоить переменным списки. Каждый список 
должен содержать имена друзей. У джона свой список друзей а у Марты свой. Друзья (имя друга) могут 
быть обычные строки “James”, “Peter” и т. Д.
"""
john_friends = ["Luk", "Bob", "Sam", "Lisa"]
marta_friends = ["Lucy", "Melany", "Samantha", "Ray"]

"""
6. Создать список с именами людей, в нем должны повторяться некоторые имена. 
Превратите список с повторяющимися именами в список уникальных имен используя множества.
"""
list_with_duplicate_names = ["Chuck", "Ozzy", "Chuck", "Robin", "Batman", "Batman", "Batman"]
list_with_names = list(set(list_with_duplicate_names))

"""
7. Создайте 2 переменные типа кортеж. Кортеж должен состоять из 2 чисел с плавающей точкой. 
Первое значение кортежа это широта в которой вы проживаете, а второе это долгота в которой вы проживаете.
"""
tuple_1 = (46.4625565, 30.74601465)

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
