"""
1 Описать любой объект на ваш выбор в классе. Хочу что бы объект распечатывался в консоль в следующем формате:

class_name: {

key: value

}

Где class_name - имя вашего класса, key - имя поля, value - значение поля.
"""
from car_prius import CarPrius

if __name__ == '__main__':
    prius = CarPrius()
    print(prius)
