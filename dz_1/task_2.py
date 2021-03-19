i = 1
cube_list = []
while i <= 1000:
    cube_list.append(i**3)   # для решения задачи под пунктом b) i**3 нужно заменить на i+17, просто не стал копировать код
    i += 2 

#cube_list = [11,55,48,37,77,777]   # для проверки
list_1 = []                        # список хранящий решение задачи 

while cube_list != []:
    t = [cube_list.pop()]      # t это список хранящий в себе последний элемент из списка cube_list
    t = str(t[0])              
    sum = 0                    
    i = 0                      # i счетчик 
    while i < len(t):
        sum = sum + int(t[i])  # sum хранит сумму чисел, отдельно взятого элемента 658 : 6+5+8 = 19
        i += 1 
    if sum%7 == 0:
        list_1.append(sum)
          
list_1.reverse()    
print(list_1)






    
 
