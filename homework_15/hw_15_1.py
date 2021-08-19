"""
Описать объект на ваше усмотрение. Экземпляр объекта может быть лишь один в системе.
Хочу увидеть паттерн синглтон но статическое поле инстанс хочу видеть приватным.
"""
from homework_15.car_singleton import singleton


@singleton
class Car:
    def __init__(self, name: str, color: str, body_type: str, engine_type: str):
        self.__wheels = 4
        self.__engine = True
        self.__name = name
        self.__color = color
        self.__body_type = body_type
        self.__engine_type = engine_type


if __name__ == '__main__':
    prius = Car("Prius", "Green", "Hatchback", "Hybrid")
    bmw = Car("BMW", "Yellow", "Sedan", "Petrol")
    print(prius)
    print(bmw)
