#Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
#русский язык. Например:
#Если перевод сделать невозможно, вернуть None.
#Доработать предыдущую функцию в num_translate_adv(): реализовать
#корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
#должен быть с заглавной

def num_translate_adv(num):
    if num.istitle():
        print(str(number.get(num.lower())).title())
    else:
        print(number.get(num))

number = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь'
}

num = input('Введите число:')
num_translate_adv(num)

