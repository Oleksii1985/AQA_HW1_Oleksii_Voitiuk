"""
Создайте функцию которая способна вернуть квадраты четных элементов для диапазона от 0 до 1000000000 включительно.
Решение должно отрабатывать и не фризить ваш комп.
"""


def my_gen():
    counter = 0
    while counter < 1000000000:
        if counter % 2 == 0:
            yield counter
        counter += 1


generator = my_gen()
print(next(generator))
print(next(generator))
print(next(generator))


result = (item ** 2 for item in range(0, 1000000001) if item % 2 == 0)


# Well nice but I suggest use generator function or comprehension but not
# all in one
# -1 point
