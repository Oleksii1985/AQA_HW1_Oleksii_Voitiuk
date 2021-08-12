from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def get_product(self, name: str):
        pass

    # Well product should be parent for all products like applica, banana and etc.
