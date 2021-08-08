from action import Action


class Human:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        self.__action: Action = Action()

    @property
    def name_human(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def action(self) -> Action:
        return self.__action
