from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def get_product(self, name: str):
        pass
