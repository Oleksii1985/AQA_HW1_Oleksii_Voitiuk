class CarPrius:
    def __init__(self):
        self.__wheels = 4
        self.__doors = 4
        self.__engine = True
        self.__engine_type = "Hybrid"
        self.__car_body_type = "Hatchback"
        self.__fuel_type = "Petrol"

    def __str__(self):
        return (
            f"{self.__class__.__name__}\n"
            f"{self.__dict__}"
        )
