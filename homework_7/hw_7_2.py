"""
Написать свою реализацию функции map
Примечание: задачи 1-3 должны иметь следующую сигнатуру def function_name(callback, sequence).
Аннотации дописать самим. Функции должны уметь работать с целыми числами, числами с плавающей точкой и
строками в качестве элементов последовательностей. В качестве последовательностей могут быть переданы списки,
кортэжи, словари. Буду проверять с помощью майпай аннотации.
"""
from typing import Union, Callable, Dict, List, Tuple


def my_map(callback: Callable, sequences: Union[Dict, List, Tuple]):
    res = []
    for elem in sequences:
        res.append(callback(elem))
    return res


john = {"name": "John", "age": 23, "gender": "Male"}
james = {"name": "James", "age": 12, "gender": "Male"}
marta = {"name": "Marta", "age": 56, "gender": "Female"}

print(my_map(lambda n: n ** 2, [1, 4, 56, 7, 87]))
print(my_map(lambda n: f"Hello {n}", ["James", "Marta", "John"]))
print(
    my_map(
        lambda man: (man["name"], man["age"]),
        [john, james, marta]
    )
)
