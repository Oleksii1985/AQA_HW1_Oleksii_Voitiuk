"""
Реализовать библиотеку с любым функционалом. К примеру создайте функции для арифметических операций и
выстроите фасад из импортов. Хочу иметь возможность импортировать кое какие функции из пакета но не все.
"""
from arithmetic_functions import addition, subtraction, multiply


if __name__ == '__main__':
    print(addition(5, 5))

# Well good. But I am expected to see arithmetic functions inside some package
# But it is also good.
