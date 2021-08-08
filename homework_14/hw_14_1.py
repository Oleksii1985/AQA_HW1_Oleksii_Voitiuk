"""
Создать класс Action. класс должен содержать название действия. Создать класс Human где в конструкторе
инстанцировать класс действие и присвоить ссылку для поля инстанса Human (поле приватное).
Написать свойство возвращающее действие. Перебрать список людей созданных с помощью класса Human
и вызвать действие как функцию.
"""
from action import Action
from human import Human

if __name__ == '__main__':
    human = Human("Alex", 36)
    action = Action()
    print(human.action.name_action)
    print(action.name_action)
    print(human.name_human)
    print(human.age)
