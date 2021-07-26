"""
Создайте класс с описанием любой компании. К примеру тошиба или глобал лоджик. Company.

Буду оценивать полноту описанного класса и буду снимать за все лишнее балы. Хочу видеть чистый код.
Ожидажю увидеть чистый код с аннотациями. Пока что без связей первого класса со вторым.
Во всех методах ожидаю увидеть докстринги с вменяемым описанием.
"""


class SomeCompany:
    def __init__(self, address: str, quantity_of_employees: int, product_name: str, telephone_number: int):
        self.__address = address
        self.__quantity_of_employees = quantity_of_employees
        self.__product_name = product_name
        self.__telephone_number = telephone_number

    def get_address(self):
        """ Return address of company """
        return self.__address

    def get_quantity_of_employees(self):
        """ Return quantity of employees in the company """
        return self.__quantity_of_employees

    def get_product_name(self):
        """ Return company's name of product """
        return self.__product_name

    def get_telephone_number(self):
        """ Return company's telephone number """
        return self.__telephone_number

    def modify_address(self, new_address: str) -> None:
        """ Modify address of company otherwise return None"""
        self.__address = new_address

    def modify_quantity_of_employees(self, new_quantity_of_employees: int) -> None:
        """ Modify quantity of employees in the company otherwise return None"""
        self.__quantity_of_employees = new_quantity_of_employees

    def modify_product_name(self, new_product_name: str) -> None:
        """ Modify company's name of product otherwise return None"""
        self.__product_name = new_product_name

    def modify_telephone_number(self, new_telephone_number: int) -> None:
        """ Modify company's telephone number otherwise return None"""
        self.__telephone_number = new_telephone_number
