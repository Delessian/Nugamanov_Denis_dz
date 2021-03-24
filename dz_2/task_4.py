list_1 = ['инженер-конструктор Игорь', 'главный бугалтер МАРИНА', 
    'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']

for i in range(len(list_1)):
    list_1[i] = list_1[i].split()
    list_1[i] = f'Привет, {(list_1[i][-1]).capitalize()}!'
    print(list_1[i])

print(list_1)
    
    
