from functools import wraps

def maxim(mx):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **wpargs):
            result = func(*args, **wpargs)
            if result > mx:
                print(func.__name__, args, *wpargs, 'Result is too big {0}. Max allowed is {1}.'.format(result, mx) )
            return result
        return wrapper 
    return deco   
                
                
@maxim(100000)
def cube(n):
    return n ** 3 

print()
print('{:.4f}'.format(cube(125)), 'C')             
print()   