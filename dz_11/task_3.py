class OnlyNumber:
    @staticmethod 
    def list_number():
        list_number = []
        print(f'Сформируйте список только из чисел !!!\nДля вывода списка введите "stop"')
        while True:
            number = input('Введите число: ')
            if number == 'stop':
                break
            else:
                try:
                    number = float(number)
                    list_number.append(number)
                except ValueError:
                    print('Нужно ввести число !!!')
                    continue   
        print(list_number)
    

a = OnlyNumber()
a.list_number()
