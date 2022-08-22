#Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
number = int(input("Введите число: "))
import math
math.factorial(number)
sequence = [math.factorial(i+1) for i in range(number)]
print(f"Список из  N членов последовательности: {sequence}")
