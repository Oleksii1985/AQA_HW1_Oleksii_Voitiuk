from .train_car import TrainCar


class Train:
    def __init__(self):
        self.__train_cars = []

    def __len__(self):
        return len(self.__train_cars)

    def add_train_car(self, train_car: TrainCar):
        return self.__train_cars.append(train_car)

    @property
    def train_cars(self):
        return self.__train_cars
