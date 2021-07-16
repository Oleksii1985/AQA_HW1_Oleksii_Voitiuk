"""
Написать свою реализацию функции reduce
Примечание: задачи 1-3 должны иметь следующую сигнатуру def function_name(callback, sequence).
Аннотации дописать самим. Функции должны уметь работать с целыми числами, числами с плавающей точкой и
строками в качестве элементов последовательностей. В качестве последовательностей могут быть переданы списки,
кортэжи, словари. Буду проверять с помощью майпай аннотации.
"""
from typing import Union, Callable
list_1 = [10, 15, 25, 40, 10]


def my_reduce(callback: Callable, *sequences: Union[dict, list, tuple]) -> Union[int, float, str]:
    return callback(sequences)


def add(a, b):
    return a + b


a = list_1
for i in range(1, len(list_1)):
    b = list_1[i]
    a = add(a, b)
