income_dir = {
    'wage': 100,
    'bonus': 20
}

class Worker:
    def __init__(self, name, surname, position, income=income_dir):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income
 
class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname} : {self.position}')
    def get_full_income(self):
        _income = self.income.get('wage') + self.income.get('bonus')
        print(_income)
             
#a = Position('Костя', 'Петров', 'Инженер')
#a.get_full_name()
#a.get_full_income()


