"""
2 Описать объект Train. Класс должен содержать поля и метод добавления вагонов
(добавлять нужно именно обьекты экземпляры класса вагон). Описать вместе с поездом класс TrainCar (вагон).
Вагон должен содержать список пассажиров и позволять добавлять пассажиров. В вагоне может быть 10 пассажиров к примеру.
 При использовании функции len на вагоне хочу видеть количество пассажиров. При использовании len на поезде
 хочу видеть список вагонов без локомотива. У каждого вагона должен быть номер. При принте вагона в консоль
 хочу видеть следующее "[n]" где n номер вагона.
"""
from train import Train
from train_car import TrainCar

if __name__ == '__main__':
    train = Train()
    train_car = TrainCar()

    train.add_train_car(1)
    print(len(train))
    train.add_train_car(15)
    print(len(train))
    print(train.train_cars[1])

    train_car.add_passenger(10)
    print(len(train_car))
    train_car.add_passenger(1)
    print(len(train_car))
    train_car.add_passenger(3)
    print(len(train_car))
    print(train_car.passengers_list)
    print(train_car.capacity)
