import time 

class TrafficLight:
    _color = 'цвет'
    
    @staticmethod
    def running(**kwargs):
        for key, val in kwargs.items():
            TrafficLight._color = key
            print(key) 
            time.sleep(val)
   
a = TrafficLight()
a = a.running(красный=7, желтый=2, зеленый=1)
