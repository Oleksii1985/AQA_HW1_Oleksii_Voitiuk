"""
Написать свою реализацию функции map
Примечание: задачи 1-3 должны иметь следующую сигнатуру def function_name(callback, sequence).
Аннотации дописать самим. Функции должны уметь работать с целыми числами, числами с плавающей точкой и
строками в качестве элементов последовательностей. В качестве последовательностей могут быть переданы списки,
кортэжи, словари. Буду проверять с помощью майпай аннотации.
"""
from typing import Union, Callable


def my_map(callback: Callable, *sequences: Union[dict, list, tuple]) -> Union[int, float, str]:
    res = []
    if len(sequences) > 0:
        min_l = min(len(sub_seq) for sub_seq in sequences)
        for elem in range(min_l):
            res.append(callback(*[sub_seq[elem] for sub_seq in sequences]))
    return callback(res)
