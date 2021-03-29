list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 
          'воздуха', 'была', '+5', 'градусов']

for i in range(len(list_1)):
    try:
        if type(int(list_1[i])) == int and len(list_1[i]) == 1:
            list_1[i] = '0'+list_1[i]
        if '+' in list_1[i] and len(list_1[i]) == 2:
            list_1[i] = '+0'+str(int(list_1[i]))
    except ValueError:
        continue

print(' '.join(list_1))
