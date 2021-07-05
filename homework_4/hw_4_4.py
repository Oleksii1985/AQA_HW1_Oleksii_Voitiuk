"""
4 у вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"]
преобразовать его в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"]
"""
import re
some_list = ["FirstItem", "FriendsList", "MyTuple"]
new_list = []
for str_ in some_list:
    new_list.append(re.sub('(?!^)([A-Z]+)', r'_\1', str_).lower())
