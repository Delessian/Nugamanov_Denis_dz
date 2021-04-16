
def val_checker(func_ch):
    def _checker(func):
        def wrapper(args):
            assert func_ch(args), f'wrong value {args}'
            result_func = func(args)
            return result_func
        return wrapper
    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x**3
        
     
print(calc_cube(5))
#print(calc_cube(-8))


