# ===========================================================
#                      Evolutive 3
# ===========================================================
print('=' * 94 + '\n') 

class FilterFuncs:
    
    def __init__(self, vt):
        self.v = vt
        
    def filter_ints(self):
        return [num for num in self.v if self.is_positive(num)]

    def filter_ints_n(self):
        return [num for num in self.v if not self.is_positive(num) and num != 0]

    @staticmethod
    def is_positive(n):         
        return n > 0        
       
    def prsen(self):
        print('is positive:', self.v)
        for n in self.v:
            print(('{}\t{}'.format(n, self.is_positive(n))))
              

v1 = [33, -44, 0, -50, 80, -11, 22]
v2 = [43, -54, 0, -60, 91, -21, 32]
ff1 = FilterFuncs(v1)
ff2 = FilterFuncs(v2)

ff1.prsen()
print('positive list: {}'.format(ff1.filter_ints()))  
print('negative list: {}'.format(ff1.filter_ints_n()))
print()

ff2.prsen()
print('positive list: {}'.format(ff2.filter_ints()))  
print('negative list: {}'.format(ff2.filter_ints_n()))
print()



print('\n' + '=' * 94) 





