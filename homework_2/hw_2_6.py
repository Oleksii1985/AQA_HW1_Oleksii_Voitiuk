"""
У вас есть группа людей с неуникальными именами.
Сформируйте список не повторяющихся имен (для этой задачи нельзя использовать set. Если в списке есть 2 джона
нужно взять лишь одного из них. "John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow")
"""
list_of_guests = ["Anna Smith", "John Snow", "Bob Mann", "John Snow", "Phil Lane", "Lisa Bum"]
unique_list = [item for pos, item in enumerate(list_of_guests) if list_of_guests.index(item) == pos]
