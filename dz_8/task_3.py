def type_loger(func):
    def wrapper(*args, **kwargs):
        result_func = func(*args, **kwargs)
        if kwargs != {}:
            for i in args:
                for key, val in kwargs.items():
                    return f'{result_func}\n{i}:{type(i)}\n{key}:{val},{type(val)}'
        else:
            for i in args:
                return f'{result_func}\n{i}:{type(i)}'    
    return wrapper


@type_loger
def calc_cube(x):
    return x**3
        
     
print(calc_cube(5))

