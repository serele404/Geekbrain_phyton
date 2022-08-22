#Задача 3. Реализуйте алгоритм перемешивания списка.
import random
num = int(input("Введите количество чисел в списке: "))
x = list(range(0, num))
random.shuffle(x)
print(x)

