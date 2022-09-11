#Задача 4. (25) Написать программу преобразования десятичного числа в двоичное

num_decimal = int(input("Введите десятичное число: "))
num_binary = ''
while num_decimal > 0:
    num_binary = str(num_decimal % 2) + num_binary
    num_decimal = num_decimal // 2
print(f"Число в двоичной системе счисления составляет: {num_binary}")
