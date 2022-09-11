#Задача 5. (26) 26.	Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
 #Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

n = int(input('Введите число: '))

def fibonacci(n):
    fibo_sequence = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_sequence.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n):
        fibo_sequence.insert(0, a)
        a, b = b, a - b
    return fibo_sequence

print(fibonacci(n))

