#Задача 2. (23) Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

num = input("Введите целое число через пробел: ")
lst = list(str(num).split(' '))
print(lst)
lst_int = list(map(int, lst))
print(lst_int)
values = []
unique_values = []
for i in range(0, len(lst_int)):
   n = lst_int[i] * lst_int[-1 - i]
   if n not in values:
        values.append(n)
print(values)

