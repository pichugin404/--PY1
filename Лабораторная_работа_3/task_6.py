list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_value = max(list_numbers)  # максимальное значение в списке
max_i = 0  # индекс максимального значения

for i, current_value in enumerate(list_numbers):  # цикл поиска максимального индекса
    if current_value == max_value:  # условие поиска максимального индекса
        max_i = i

list_numbers[max_i], list_numbers[-1] = list_numbers[-1], list_numbers[max_i]  # смена местами

print(list_numbers)
