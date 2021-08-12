from typing import Type


def singleton(_class: Type):
    def inner(*args: str):
        if not hasattr(_class, "__instance"):
            setattr(_class, "__instance", _class(*args)) # well this attribute is not private) private attribute contain tame of class
        return getattr(_class, "__instance")
    return inner
