from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes_list = []

def get_jokes(count):
    for i in range(count):
        jokes = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        jokes_list.append(jokes)
    print(jokes_list)

get_jokes(3)
