number = int(input("Введите любое целое число: "))
if abs(number) == 2 or abs(number) == 3 or abs(number) == 4:
    print("{} процента".format(number))
elif abs(number) == 1:
    print("{} процент".format(number))
else:
    print("{} процентов".format(number))
