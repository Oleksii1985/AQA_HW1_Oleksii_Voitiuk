"""
Написать свою реализацию функции reduce
Примечание: задачи 1-3 должны иметь следующую сигнатуру def function_name(callback, sequence).
Аннотации дописать самим. Функции должны уметь работать с целыми числами, числами с плавающей точкой и
строками в качестве элементов последовательностей. В качестве последовательностей могут быть переданы списки,
кортэжи, словари. Буду проверять с помощью майпай аннотации.
"""
from typing import Union, Callable, Dict, List, Tuple


def my_reduce(callback: Callable, sequences: Union[Dict, List, Tuple], initializer=None):
    it = iter(sequences)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = callback(value, element)
    return value


print(my_reduce(lambda a, b: a + b, [1, 2, 3, 4, 5]))
print(my_reduce(lambda a, b: a if a > b else b, [1, 2, 3, 4, 5]))
print(my_reduce(lambda a, b: a if a < b else b, [1, 2, 3, 4, 5]))
print(my_reduce(lambda a, b: a + b, ["One", "Two"]))
