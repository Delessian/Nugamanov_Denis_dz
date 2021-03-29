translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'night': 'девять',
    'ten': 'десять'
}
def num_translate(key):
    if key == key.capitalize():
        key = key.lower()
        print(translate.get(key).capitalize())
    else:
        print(translate.get(key))   
    
num_translate('One')
num_translate('one')
num_translate('Six')
num_translate('six')
num_translate('eleven')

