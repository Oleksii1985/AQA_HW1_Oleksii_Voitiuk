"""
У вас есть 3 группы людей bigno_blacklist, poker_blacklist, majong_blacklist.
Имена людей в формате "John Dow" первое и второе имя. Найти тех кто состоит во всех черных списках
"""
bigno_blacklist = ["Anna Smith", "John Snow", "Bob Mann"]
poker_blacklist = ["John Snow", "Phil Lane", "Lisa Bum"]
majong_blacklist = ["Eric Dow", "Melanie C", "John Snow"]
same_people = set(bigno_blacklist).intersection(poker_blacklist, majong_blacklist)
