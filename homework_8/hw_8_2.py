"""
Создайте функцию которая способна вернуть квадраты четных элементов для диапазона от 0 до 1000000000 включительно.
Решение должно отрабатывать и не фризить ваш комп.
"""


def square_is_even():
    result = (item ** 2 for item in range(0, 1000000001) if item % 2 == 0)
    for item in result:
        return item

# Well it is also will wor;k but there is no need to use generator
# comprehension inside function. Use of comprehension or generator function
# instead

# -2 points
