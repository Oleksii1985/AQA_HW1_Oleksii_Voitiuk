class Action:
    def __init__(self):
        self.__name: str = "Jogging"

    @property
    def name_action(self) -> str:
        return self.__name
