"""
Используя созданный файл в задаче 1 прочитать файл и произвести математические операции над каждым элементом.
Результат операции вывести в консоль. Использовать импорты для импортирования из модуля первой задачи нельзя.
"""
import pickle
with open("test/data/file.txt", 'rb') as file:
    operations = pickle.load(file)
for operation in operations:
    left_operand, right_operand, operator = operation
    if operator == 1:
        print(f"Tuple is: {operation} result is: {left_operand} + {right_operand} = {left_operand + right_operand}")
    elif operator == 2:
        print(f"Tuple is: {operation} result is: {left_operand} - {right_operand} = {left_operand - right_operand}")
    else:
        print(f"Tuple is: {operation} result is: {left_operand} * {right_operand} = {left_operand * right_operand}")
