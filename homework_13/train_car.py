class TrainCar:
    def __init__(self, number):
        self.__number = number
        self.__capacity = 10
        self.__passengers_list = []

    def __len__(self):
        return len(self.__passengers_list)

    def __str__(self):
        return f"This is number of TrainCar: {self.__number}"

    def add_passenger(self, number_ticket: int):
        if len(self.__passengers_list) < self.__capacity:
            self.__passengers_list.append(number_ticket)
        else:
            print(f"TrainCar has maximum capacity: {self.__capacity}")
        return self.__passengers_list

    @property
    def passengers_list(self):
        return self.__passengers_list

    @property
    def capacity(self):
        return self.__capacity
