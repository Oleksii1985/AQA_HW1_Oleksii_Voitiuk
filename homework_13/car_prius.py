class CarPrius:
    def __init__(self):
        self.__wheels = 4
        self.__doors = 4
        self.__engine = True
        self.__engine_type = "Hybrid"
        self.__car_body_type = "Hatchback"
        self.__fuel_type = "Petrol"

    def __clean_method(self, item) -> str:
        result = item.replace(f"_{self.__class__.__name__}__", "")
        return result

    def __str__(self):
        res = ""
        for key, value in self.__dict__.items():
            res += f"{self.__clean_method(key)}: {value}\n\t"
        return (
            f"{self.__class__.__name__}:{{\n"
            f"\n\t{res}\n}}"
        )
