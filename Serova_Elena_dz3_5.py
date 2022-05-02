#Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
#случайных слов, взятых из трёх списков (по одному из каждого):
#nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#adjectives = ["веселый", "яркий", "зеленый", "утопичный","мягкий"]
#Например:
#>>> get_jokes(2)
#["лес завтра зеленый", "город вчера веселый"]


from random import randrange

def get_jokes(n):
    joke_list = []
    for i in range(n):
        joke = ' '.join([nouns[randrange(len(nouns))], adverbs[randrange(len(adverbs))], adjectives[randrange(len(adjectives))]])
        joke_list.append(joke)
    print(joke_list)
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(2)

