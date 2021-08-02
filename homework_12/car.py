from something_driving import SomethingDriving


class Car(SomethingDriving):
    def __init__(self):
        self.__wheels = 4
        self.__doors = 4
        self.__engine = True
        self.__type_of_engine = "Diesel"
        self.__engine_status = False
        super().__init__()

    def engine_status(self):
        return self.__engine_status

    def start_engine(self):
        self.__engine_status = True

    def stop_engine(self):
        self.__engine_status = False
