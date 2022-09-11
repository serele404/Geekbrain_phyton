#Задача 1. (22) Найти сумму чисел списка стоящих на нечетной позиции

def even_items(iterable):
    values = []
    for index, value in enumerate(iterable, start=1):
        if not index % 2:
            values.append(value)
    return values

num = input("Введите целое или вещественное число через пробел: ")
lst = list(str(num).replace(',', '.').split(' '))
print(lst)
lst_float = list(map(float, lst))
print(lst_float)
print(even_items(lst_float))
sum_lst = sum(even_items(lst_float))
print(sum_lst)

