"""
Создайте итератор принимающий последовательность и умеющий перебирать значения по заданному диапазону.
CustomIterator(sequence, start_index, end_index)
"""


class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__start_index = start_index - 1
        self.__end_index = end_index
        self.__sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        self.__start_index += 1
        if self.__sequence[self.__start_index] < len(self.__sequence):
            if self.__sequence[self.__start_index] == self.__sequence[self.__end_index]:
                raise StopIteration
            num = self.__sequence[self.__start_index]
            return num
        else:
            raise StopIteration


if __name__ == '__main__':
    custom_iterator = CustomIterator([1, 2, 3, 4, 5, 6, 7], 3, 6)
    iterator = iter(custom_iterator)

    for item in iterator:
        print(item)
