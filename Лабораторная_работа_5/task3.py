from random import sample  # импорт функции sample из модуля random

L = -10  # левая граница диапозона
R = 10  # правая граница диапозона
len_list = 15  # размер списка чисел


def get_unique_list_numbers() -> list[int]:
    """Функция, которая возвращает список, заполненный случайными целыми числами.
    Числа в списке уникальные. """

    # формируется список чисел с заданнаными границами
    spisok = [i for i in range(L, R+1)]
    # выборка случайных уникальных чисел нужного количества
    random_values = sample(spisok, k=len_list)

    return random_values


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
