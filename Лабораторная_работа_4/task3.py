# ФУНКЦИЯ ДЛЯ УДАЛЕНИЯ СИМВОЛА ПО НУЖНОМУ ИНДЕКСУ ( ПО УМОЛЧАНИЮ УДАЛЯЕТСЯ ПОСЛЕДНИЙ ЭЛЕМЕНТ)
def delete1(list_, index=None):
    if index is None:  # условие, если не был задан индекс пользователем
        new_list = list_[:-1]  # создается новый список без последнего элемента
    else:
        left_list = list_[:index]  # создается новый список от левой границы до заданного индекса
        right_list = list_[index + 1:]  # создается новый список от заданного индекса до правой границы
        new_list = left_list + right_list  # складывается левая часть и правая часть

    return new_list


# ФУНКЦИЯ ДЛЯ УДАЛЕНИЯ ПОСЛЕДНЕГО СИМВОЛА И СИМВОЛА ПО НУЖНОМУ ИНДЕКСУ ( ПО УМОЛЧАНИЮ УДАЛЯЕТСЯ ПОСЛЕДНИЙ ЭЛЕМЕНТ)

def delete2(list_, index=None):
    if index is None:
        new_list = list_[:-1]
    else:
        left_list = list_[:index]
        right_list = list_[index + 1:-1]
        new_list = left_list + right_list

    return new_list


print(delete1([0, 0, 1, 2], index=0))  # [0, 1]
print(delete1([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete1([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
