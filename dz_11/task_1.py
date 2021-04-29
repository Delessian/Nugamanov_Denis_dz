class Date:
    def __init__(self, date):
        self.date = date
        Date.date = date
    
    @classmethod
    def output_date(cls):
        date_list = cls.date.split('-')
        cls.number = int(date_list[0])
        cls.month = int(date_list[1])
        cls.year = int(date_list[2])
        
    @staticmethod
    def valid_date():
        assert (0 < Date.month <= 12), f'wrong month: {Date.month}'
        assert (0 < Date.number <= 31), f'wrong date: {Date.number}'

        
a = Date('32-12-1993')
a.output_date()
a.valid_date()
print(Date.number)
