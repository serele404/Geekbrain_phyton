
#Реализовать склонение слова «процент» во фразе «N процентов».
#Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
#1 процент
#2 процента
#3 процента
#4 процента
#5 процентов
#6 процентов
#...
#100 процентов

for i in range(1,101):
    new_list = list(str(i))
    if int(new_list[-1]) == 1 and i != 11:
        print('{} процент'.format(i))
    elif i> 10 and i<= 14:
        print('{} процентов'.format(i))
    elif int(new_list[-1])>1 and int(new_list[-1])<= 4:
        print('{} процента'.format(i))
    else:
        print('{} процентов'.format(i))

