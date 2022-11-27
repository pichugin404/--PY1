import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter: str = ',', new_line: str = '\n') -> list[dict]:
    """ Функция, которая конвертирует из csv в json формат.

            Подробное описание функции.

            Args:
                filename: название импортируемого файла.
                delimiter : разделитель между значениями, по умолчанию ","
                new_line : разделитель строк, по умолчанию "\n".

            Returns:
                Возвращаем список словарей сформиронный из входных данных

            """
    with open(filename) as f:  # открываем импортируемый файл
        # разделяем строки запятой и заменяем "\n" на " "
        dat = [line.replace(new_line, '').split(delimiter) for line in f]

        keys = dat[0]  # говорим, что первая строка это ключи

    res_list = []  # пустая строка

    for i in range(1, len(dat)):  # задаем цикл от 1 до длины списка строк
        result = dict(zip(keys, dat[i]))   # создаем словари где объединеям ключи и значения
        res_list.append(result)  # формируем список словарей

    return res_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
