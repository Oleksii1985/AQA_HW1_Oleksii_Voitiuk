"""
3 есть строка переданная в качестве квери параметров
"     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             ".
Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары
значение после равно {name: Amanda......}
"""
some_string = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "
new_string = some_string.strip()
pairs = new_string.split("=")
dict(zip(pairs[::2], pairs[1::2]))
