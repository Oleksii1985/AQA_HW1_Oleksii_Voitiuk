"""
Описать транспортное средство. Можете брать любое на свое усмотрение.
Хочу видеть наследование (обычное с несколькими уровнями иерархии), абстракцию, сокрытие, инкапсуляцию.
"""
from abc import ABC, abstractmethod


class AutoMachine(ABC):
    def __init__(self):
        self.wheels = 4
        self.doors = None
        self.type_of_auto = None
        self.color = None
        self.engine = True
        self.type_of_engine = None

    @staticmethod
    def moving_forward():
        print("I'm moving forward ...")

    @staticmethod
    def moving_backward():
        print("I'm moving backward ...")

    @staticmethod
    def stopping():
        print("I'm stopping ...")

    @staticmethod
    def __special_equipment():
        print("This is only for rally cars")

    def _equipment_for_rally(self):
        self.__special_equipment()

    @abstractmethod
    def refuel(self):
        """Logic depends of type of engine"""


class GasolineSedanCar(AutoMachine):
    def __init__(self):
        self.doors = 4
        self.type_of_auto = "Sedan"
        self.type_of_engine = "Gasoline"
        super().__init__()

    def refuel(self):
        print("I'm using gasoline ...")


class RallyCar(GasolineSedanCar):
    def __init__(self):
        self.doors = 2
        self.color = "Red"
        super().__init__()
