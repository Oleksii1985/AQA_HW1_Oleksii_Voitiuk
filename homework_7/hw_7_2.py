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
