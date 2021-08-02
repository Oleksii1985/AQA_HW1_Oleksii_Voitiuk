"""
Опишите любой объект на ваш выбор в классе. Основные требования к объекту:
объект должен содержать некое поведение которое меняет его состояние
объект должен быть простым то бишь только по средством своего поведения менять свое состояние.
должны присутствовать следующие постулаты: абстракция, наследование, инкапсуляция, сокрытие
Проявите свою фантазия. Балы сильно снимать не буду.
"""
from car import Car

if __name__ == '__main__':
    car = Car()
    print(car.engine_status())
    car.start_engine()
    print(car.engine_status())
    car.stop_engine()
    print(car.engine_status())

# Not bad but Interface should not contain any implementation __init__ it
# is method with implementing fields
# -2 points
# Want to see more logic in future implementations