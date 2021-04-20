import random

class Car:
    def __init__(self, speed, name, is_polise = False):
        self.speed = speed
        self.name = name
        self.is_polise = is_polise
    def go(self):
        print(f'{self.name} едет')
    def stop (self):
        print(f'{self.name} остановилась')
    def turn (self):
        turn_car = {0: 'лево', 1: 'право'}
        choice = turn_car.get(random.randint(0, 1))
        print(f'{self.name} повернула на {choice}')
        
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60 and self.is_polise == False:
            print(f'Привешение скорости на {self.speed-60} км/ч')
        else:
            print(f'Скорость авто = {self.speed} км/ч')

a = TownCar(70, 'Mazda', True)
a.go()
a.stop()
a.turn()
a.show_speed()
        