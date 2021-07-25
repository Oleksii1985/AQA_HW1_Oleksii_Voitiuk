"""
Создайте функцию которая способна вернуть квадраты четных элементов для диапазона от 0 до 1000000000 включительно.
Решение должно отрабатывать и не фризить ваш комп.
"""


def square_is_even():
    result = (item ** 2 for item in range(0, 1000000001) if item % 2 == 0)
    return result

# Well nice but I suggest use generator function or comprehension but not
# all in one
# -1 point
