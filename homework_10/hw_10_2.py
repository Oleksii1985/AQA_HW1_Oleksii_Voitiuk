"""
Создайте класс с описанием работника. Любого работника. Employee.

Буду оценивать полноту описанного класса и буду снимать за все лишнее балы. Хочу видеть чистый код.
Ожидажю увидеть чистый код с аннотациями. Пока что без связей первого класса со вторым.
Во всех методах ожидаю увидеть докстринги с вменяемым описанием
"""


class Employee:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, position: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__gender = gender
        self.__position = position

    def get_first_name(self):
        """ Return first name of employee"""
        return self.__first_name

    def get_last_name(self):
        """ Return last name of employee"""
        return self.__last_name

    def get_age(self):
        """ Return age of employee"""
        return self.__age

    def get_gender(self):
        """ Return gender of employee"""
        return self.__gender

    def get_position(self):
        """ Return position of employee"""
        return self.__position

    def modify_first_name(self, new_first_name: str) -> None:
        """ Modify first name of employee otherwise return None"""
        self.__first_name = new_first_name

    def modify_last_name(self, new_last_name: str) -> None:
        """ Modify last name of employee otherwise return None"""
        self.__last_name = new_last_name

    def modify_age(self, new_age: int) -> None:
        """ Modify age of employee otherwise return None"""
        self.__age = new_age

    def modify_gender(self, new_gender: str) -> None:
        """ Modify gender of employee otherwise return None"""
        self.__gender = new_gender

    def modify_position(self, new_position: str) -> None:
        """ Modify position of employee otherwise return None"""
        self.__position = new_position

    # not bet but no logic in this class present - 2 points
    # modify methods just rewrite something but I am not sure that someone
    # outside from global scope should be able modify something -2 points
