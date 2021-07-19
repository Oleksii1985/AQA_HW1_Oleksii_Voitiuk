"""
Написать свою реализацию функции filter
Примечание: задачи 1-3 должны иметь следующую сигнатуру def function_name(callback, sequence).
Аннотации дописать самим. Функции должны уметь работать с целыми числами, числами с плавающей точкой и
строками в качестве элементов последовательностей. В качестве последовательностей могут быть переданы списки,
кортэжи, словари. Буду проверять с помощью майпай аннотации.
"""
from typing import Union, Callable, Tuple, List, Dict


def my_filter(callback: Callable, sequence: Union[Tuple, List, Dict]):
    result = []
    for item in sequence:
        result.append(item) if callback(item) else None
    return result


john = {"name": "John", "age": 23, "gender": "Male"}
james = {"name": "James", "age": 12, "gender": "Male"}
marta = {"name": "Marta", "age": 56, "gender": "Female"}

print(my_filter(lambda n: n > 5, [1, 4, 56, 7, 87]))
print(my_filter(lambda n: n.startswith('J'), ["James", "Marta", "John"]))
print(
    my_filter(
        lambda man: man["name"].startswith('J'),
        [john, james, marta]
    )
)
