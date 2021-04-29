class Except:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def dividing(self):
        try:
            print(self.a/self.b)
        except ZeroDivisionError:
            print('Делитель не может быть = 0')
                

a = Except(2, 0)
a.dividing()
