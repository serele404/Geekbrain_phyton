#Задача 3. (24) 24.	В заданном списке вещественных чисел найдите разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

num = input("Введите вещественные или целые числа через пробел: ")
lst = list(str(num).replace(',', '.').split(' '))
print(lst)
lst_float = list(map(float, lst))
lst_int = list(map(int, lst_float))
print(lst_float)
print(lst_int)
lst_float_1 = []
for i in range(0, len(lst_int)):
   n = lst_float[i] - lst_int[i]
   if n !=0.0:
        lst_float_1.append(n)
print(lst_float_1)
max_number = max(lst_float_1)
print("Наибольшее число:", max_number)
min_number = min(lst_float_1)
print("Наименьше число:", min_number)
difference_number = round (max_number - min_number,3)
print("Разница между максимальным и минимальным значением дробной части элементов:", difference_number)


