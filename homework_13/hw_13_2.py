"""
2 Описать объект Train. Класс должен содержать поля и метод добавления вагонов
(добавлять нужно именно обьекты экземпляры класса вагон). Описать вместе с поездом класс TrainCar (вагон).
Вагон должен содержать список пассажиров и позволять добавлять пассажиров. В вагоне может быть 10 пассажиров к примеру.
 При использовании функции len на вагоне хочу видеть количество пассажиров. При использовании len на поезде
 хочу видеть список вагонов без локомотива. У каждого вагона должен быть номер. При принте вагона в консоль
 хочу видеть следующее "[n]" где n номер вагона.
"""
from OleksiyVoitov.AQA_HW1_Oleksii_Voitiuk.homework_13.train import Train
from OleksiyVoitov.AQA_HW1_Oleksii_Voitiuk.homework_13.train_car import \
    TrainCar

if __name__ == '__main__':
    train = Train()
    train.add_train_car(TrainCar(1))
    print(train.train_cars[0])
    # Actual: This is number of TrainCar: 1
    # Expected: [1]
    # -1 point
