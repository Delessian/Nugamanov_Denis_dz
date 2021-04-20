class Road:
    #mass = масса кв.м. асфальта (25 кг. по умол.)
    #depth = толщина асфальта (5 см. по умол.)
    @staticmethod
    def square(_lengh, _width, mass=25, depth=5):
        result = _lengh*_width*mass*depth
        print(f'{result/1000} т')
 
a = Road()
a.square(500, 20)
