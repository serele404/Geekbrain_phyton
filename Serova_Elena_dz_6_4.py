#Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
#Известно, что при хранении данных используется принцип: одна строка — один пользователь,
#разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
#и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
#в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
#записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
#скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
#меньше объема ОЗУ.
#Фрагмент файла с данными о пользователях (users.csv):
#Иванов,Иван,Иванович
#Петров,Петр,Петрович
#Фрагмент файла с данными о хобби (hobby.csv):
#скалолазание,охота
#Объём данных в файлах превышает объём
#ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
#будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
#сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
#двоеточие и пробел после ФИО:
#Иванов,Иван,Иванович: скалолазание,охота
#Петров,Петр,Петрович: горные лыжи

from itertools import zip_longest
import json

with open('Lession 6/users.csv', 'r', encoding='utf-8') as name, open('Lession 6/hobby.csv', 'r', encoding='utf-8') as hobby:
   users_hobbys_gen = ((names, hobbys) for names, hobbys in zip_longest(name.read().splitlines(), hobby.read().splitlines(), fillvalue=None))

with open('Lession 6/users_hobby_dict.txt', 'w', encoding='utf-8') as f:
     for user_hobby in users_hobbys_gen:
        f.write(f'{user_hobby[0]}: {user_hobby[1]}\n')
