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

# make no sence to extend product with market. It is almost same like extend
# car with building
# Also no return type in annotation
