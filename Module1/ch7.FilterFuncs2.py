#
#! [Alert: Deprecated method, do not use]  
#? [Query or question: Should this method be exposed in the public API?]  
#// [CommentedOut: Do not use] 
#todo [Refactor: this method so that it conforms to the API. Create some test cases]   
#* [Important: information is highlighted] 


# ===========================================================
#                      Evolutive 2
# ===========================================================
print('=' * 94 + '\n') 

class FilterFuncs:
    
    v = []
    
    def __init__(vt):
        v = vt

    @classmethod
    def filter_ints(cls):
        return [num for num in cls.v if cls.is_positive(num)]

    @classmethod
    def filter_ints_n(cls):
        return [num for num in cls.v if not cls.is_positive(num) and num != 0]

    @staticmethod
    def is_positive(n):         
        return n > 0        
    
    @classmethod
    def set_v(cls, v):
        cls.v = v
    
    @classmethod    
    def prsen(cls):
        print('is positive:', cls.v)
        for n in cls.v:
            print(('{}\t{}'.format(n, cls.is_positive(n))))
              

v1 = [33, -44, 0, -50, 80, -11, 22]
v2 = [43, -54, 0, -60, 91, -21, 32]

ff1 = FilterFuncs()

ff1.set_v(v1)
ff1.prsen()
print('positive list: {}'.format(ff1.filter_ints()))  
print('negative list: {}'.format(ff1.filter_ints_n()))
print()

ff1.set_v(v2)
ff1.prsen()
print('positive list: {}'.format(ff1.filter_ints()))  
print('negative list: {}'.format(ff1.filter_ints_n()))
print()


print('\n' + '=' * 94) 


# ===========================================================