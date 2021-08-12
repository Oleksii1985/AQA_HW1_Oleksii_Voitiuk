from .apple import Apple
from .banana import Banana
from .celery import Celery
from .product import Product
from .strawberry import Strawberry


class Market(Product):

    def get_product(self, name: str):
        if name == "Apple":
            return Apple()
        elif name == "Banana":
            return Banana()
        elif name == "Celery":
            return Celery()
        elif name == "Strawberry":
            return Strawberry()
        else:
            raise Exception("Incorrect type of product!")
