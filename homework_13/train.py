"""
2 Описать объект Train. Класс должен содержать поля и метод добавления вагонов
(добавлять нужно именно обьекты экземпляры класса вагон).
 При использовании len на поезде хочу видеть список вагонов без локомотива.
 У каждого вагона должен быть номер. При принте вагона в консоль
 хочу видеть следующее "[n]" где n номер вагона.
"""


class Train:
    def __init__(self):
        self.__train_cars = []

    def __len__(self):
        return len(self.__train_cars[1:])

    def add_train_car(self, train_car_number):
        return self.__train_cars.append(train_car_number)

    @property
    def train_cars(self):
        return self.__train_cars
