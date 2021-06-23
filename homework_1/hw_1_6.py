"""
6. Создать список с именами людей, в нем должны повторяться некоторые имена.
Превратите список с повторяющимися именами в список уникальных имен используя множества.
"""
list_with_duplicate_names = ["Chuck", "Ozzy", "Chuck", "Robin", "Batman", "Batman", "Batman"]
list_with_names = list(set(list_with_duplicate_names))

# Good. No prints should be there.
