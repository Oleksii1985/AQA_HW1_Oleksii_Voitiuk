"""
3. Написать функцию is_prime, принимающую 1 аргумент — число от 2 до 1000, и возвращающую True, если оно простое,
и False - иначе.
"""


def is_prime(number: int):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True
