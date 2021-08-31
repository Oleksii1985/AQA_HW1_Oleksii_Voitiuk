from extra_hw.iterator_for_class import CustomIterator


class Human(CustomIterator):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender


if __name__ == '__main__':
    user = Human("Alex", 36, "male")
    for k, v in user:
        print(k, "is", v)
