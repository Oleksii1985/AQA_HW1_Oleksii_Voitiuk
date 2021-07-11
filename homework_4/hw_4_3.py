"""
3 есть строка переданная в качестве квери параметров
"     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             ".
Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары
значение после равно {name: Amanda......}
"""
if __name__ == '__main__':

    some_string = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "
    new_string = some_string.strip()
    pairs = new_string.split("=")
    print(dict(zip(pairs[::2], pairs[1::2])))

# Almost right but take a look on output:
# {'name': 'Amanda', 'sssss&age': '32&&salary', '1500&currency': 'quro'} Actual
# {'name': 'Amanda=sssss', 'age': '32', 'salary': '1500', 'currency': 'quro'} Expected

# Alternative solution
# result = dict()
#
# for pair in some_string.strip().split('&'):
#     if pair:
#         key, value = pair.split('=', maxsplit=1)
#         result[key] = value
#
# print(result)