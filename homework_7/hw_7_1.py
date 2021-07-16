"""
Написать свою реализацию функции filter
Примечание: задачи 1-3 должны иметь следующую сигнатуру def function_name(callback, sequence).
Аннотации дописать самим. Функции должны уметь работать с целыми числами, числами с плавающей точкой и
строками в качестве элементов последовательностей. В качестве последовательностей могут быть переданы списки,
кортэжи, словари. Буду проверять с помощью майпай аннотации.
"""
from typing import Union, Callable


def my_filter(callback: Callable, *sequence: Union[dict, list, tuple]) -> Union[int, float, str]:
    res = []
    for elem in sequence:
        for num in elem:
            if callable(num):
                res.append(num)
    return callback(res)
