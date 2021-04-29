class ComplexNum:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, other):
        return ComplexNum(self.num + other.num)
        
    def __mul__ (self, other):
        return ComplexNum(self.num * other.num)
        
    def __str__(self):
        return f'Комплексное число: {self.num}'
        
    
#a = ComplexNum(7 + 8j)
#b = ComplexNum(-7 + 20j)
#print(a + b)
#print(a * b)

class MyComplexNum:
    def __init__(self, complex_num, list_complex = []):
        self.complex_num = complex_num
        self.list_complex = list_complex
        
        import re
        
        full_complex = r'([\d.-]+)([\D]+\s[i][\d.-]+)'
        im_complex = r'[i]'

        if re.match(full_complex, complex_num):
            result = re.findall(full_complex, complex_num)
            Re = list(*result)[0]
            Im = list(*result)[1].replace('i', '').replace(' ', '')
        elif re.search(im_complex, complex_num):
            Re = 0
            Im = complex_num.replace('i', '')
        else:
            Re = complex_num
            Im = 0
        list_complex.append(int(Re))
        list_complex.append(int(Im))
        
    def __add__(self, other):
        return MyComplexNum([i+j for i, j in zip(self.list_complex, other.list_complex)])
     
           
    def __str__(self):
        return f'\nRe: {self.list_complex[0]}\nIm: {self.list_complex[1]}'
        
        
a = MyComplexNum('20 - i10', [])
b = MyComplexNum('30 - i130', [])
print(a + b)

