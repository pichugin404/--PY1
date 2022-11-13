# импорт функций ascii_letters, digits из модуля string
from string import ascii_letters, digits
# импорт функции sample  из модуля random
from random import sample


def get_random_password(n=8) -> str:
    """ Функция для генерации случайных паролей заданной длины n (по умолчанию 8 символов)."""

    list_symbols = ascii_letters + digits  # создается буквено-численная последовательность
    pass_ = sample(list_symbols, k=n)  # выбирается n случайных символов из последовательности
    pass_ = ("".join(map(str, pass_)))  # преобразование в строку

    return pass_


print(get_random_password())
