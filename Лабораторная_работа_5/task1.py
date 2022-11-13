from pprint import pprint  # импортируем функцию pprint из модуля pprint

L = 0  # левая граница перебираемых чисел
R = 15  # правая граница перебираемых чисел

# создание списка словарей с помощью list comprehension
spisok_slov = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(L, R + 1)]

pprint(spisok_slov)  # вывод результата
