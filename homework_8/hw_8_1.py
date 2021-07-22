"""
Создать декоратор которые принтит в консоль имя функции которая была вызвана.
Функция при этом должна работать как и задумывалось. К примеру создайте пару функции для арифметических
операций суммирования и умножения. При вызове этих функций должен возвращаться результат операции и предварительно
выводиться в консоль имя функции которая была вызвана.
"""


def my_decorator(func):
    def inner(a, b):
        print(f"name of function is: {func.__name__}")
        func(a, b)
    return inner


@my_decorator
def addition(a, b):
    return a + b


@my_decorator
def multiply(a, b):
    return a * b


if __name__ == '__main__':
    print(multiply(5, 5))
    print(addition(5, 5))

# Well nice but decorator brake logic of function. Since main purpose of
# function is arithmetic operation and getting result which should be returned.
# name of function is: multiply
# None
# name of function is: addition
# None

# -3 points
