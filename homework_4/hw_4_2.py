"""
2 есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"].
выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и
форматирование через f string. Так же над именами первой строкой выведини заговловок Names где слово
names должно быть посредине а остальное пространство заполнено скажем символом "*"
"""
some_list = ["John", "Marta", "James", "Amanda", "Marianna"]
print("Names".center(36, "*"))
for name in some_list:
    print(f"{name.rjust(20)}")

# Good but you have done task using rjust method.
# Take a look on code examples for lesson 4 and try to make it using f string
# syntax without rjust

# for name in some_list:
#     print(f"{name:>20}")