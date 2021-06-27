"""
у вас есть список элементов [1, 2, 3, 4, 5, 6, 7, 8]. Перебрать список используя foreach цыкл .
Элемент с нечетным индексом поместить в новый список кортежей где первый элемент это индекс а второй это значение.
[(index, value)]. соответственно элементы с четным индексом поместить в другой список кортежей с тем же форматом
что и в случае с нечетными индексами.
"""
some_list = [1, 2, 3, 4, 5, 6, 7, 8]
list_of_tuples = list(enumerate(some_list))
odd_list_of_tuples = []
even_list_of_tuples = []
for index, value in list_of_tuples:
    if index % 2 == 0:
        even_list_of_tuples.append(value)
        list(enumerate(even_list_of_tuples))
    else:
        odd_list_of_tuples.append(value)
        list(enumerate(odd_list_of_tuples))
