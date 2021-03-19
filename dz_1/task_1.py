duration = int(input("Конвертер секунд.\nВведите количество секунд: "))
if duration < 60:
    print("{} сек.".format(duration))
elif 60 <= duration < 3600:
    min = duration//60
    sec = duration%60
    print("{} мин. {} сек.".format(min,sec))
elif 3600 <= duration < 86400:
    hour = duration//3600
    min = (duration-hour*3600)//60
    sec = duration-hour*3600-min*60
    print("{} ч. {} мин. {} сек.".format(hour,min,sec))
else:
    day = duration//86400
    hour = (duration - day*86400)//3600
    min = (duration - day*86400 - hour*3600)//60
    sec = duration - day*86400 - hour*3600 - min*60
    print("{} д. {} ч. {} мин. {} сек.".format(day,hour,min,sec))
    
    
    