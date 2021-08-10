class Action:
    def __init__(self, name: str):
        self.__name = name

    def __call__(self):
        print(f"I'm {self.__name}")
