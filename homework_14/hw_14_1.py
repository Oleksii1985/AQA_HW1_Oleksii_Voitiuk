"""
Создать класс Action. класс должен содержать название действия. Создать класс Human где в конструкторе
инстанцировать класс действие и присвоить ссылку для поля инстанса Human (поле приватное).
Написать свойство возвращающее действие. Перебрать список людей созданных с помощью класса Human
и вызвать действие как функцию.
"""
from homework_14.action import Action
from homework_14.human import Human

if __name__ == '__main__':
    action = Action("jogging")
    human = Human("Alex", 36, action)

    human.action()
