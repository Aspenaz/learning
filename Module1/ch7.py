
# ===========================================================
# ===========================================================
#             Testing, Profiling, and
#             Dealing with Exceptions
# ===========================================================
# ===========================================================




# ===========================================================
#                Writing a unit test
# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\tdata.py\n')

def get_clean_data(source):
    data = load_data(source)
    cleaned_data = clean_data(data)
    return cleaned_data

print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\tfilter_funcs.py\n')

def filter_ints(v):
    return [num for num in v if is_positive(num)]

def filter_ints_n(v):
    return [num for num in v if not is_positive(num) and num != 0]

def is_positive(n):         
    return n > 0            # Return boolean value.


v = [3, -4, 0, -5, 8]

positive_l = list(filter_ints(v))
negative_l = list(filter_ints_n(v))

print('is positive:')
for n in v:
    print('{}\t{}'.format(n, is_positive(n)))

print()

print('positive list: {}'.format(positive_l))  
print('negative list: {}'.format(negative_l))  


print('\n' + '=' * 94) 


# ===========================================================
#                     Evolutive 1
# ===========================================================
print('=' * 94 + '\n') 


class FilterFuncs:
    
    def __init__(self, v):
        self._v = v
    
    def filter_ints(self):
        return [num for num in self._v if FilterFuncs.is_positive(num)]

    def filter_ints_n(self):
        return [num for num in self._v if not FilterFuncs.is_positive(num) and num != 0]

    @staticmethod
    def is_positive(n):         
        return n > 0            # Return boolean value.
    
    
v = [3, -4, 0, -5, 8]
filter1 = FilterFuncs(v)

print('v = {} \n'.format(filter1._v))

print('is positive:')
for n in filter1._v:
    print('{}\t{}'.format(n, filter1.is_positive(n) ))
print()

positive_l = list(filter1.filter_ints()) 
negative_l = list(filter1.filter_ints_n()) 

print('positive list: {}'.format(positive_l))  
print('negative list: {}'.format(negative_l))  


print('\n' + '=' * 94) 


# ===========================================================
#                      Evolutive 2
# ===========================================================
print('=' * 94 + '\n') 


class FilterFuncs:
    v1 = [30, -40, 0, -50, 80, ]
    
    def __init__(self, _v):
        self._v = _v
    
    @classmethod    
    def change_v(cls):
        cls.v1 = cls.get_v()
        # return cls.v1

    @classmethod
    def filter_ints(cls):
        cls.change_v()
        return [num for num in cls.v1 if cls.is_positive(num)]

    @classmethod
    def filter_ints_n(cls):
        return [num for num in cls.v1 if not cls.is_positive(num) and num != 0]

    @staticmethod
    def is_positive(n):         
        return n > 0            # Return boolean value.
    
    # @staticmethod
    def get_v(self):
        # print('v1:', FilterFuncs.v1)
        return self._v
    
v = [3, -4, 0, -5, 8]
ff1 = FilterFuncs(v)

print('_v = {} \n'.format(ff1._v))
print('v1 = {} \n'.format(ff1.v1))
# ff1.change_v()
print('v1(_v) = {} \n'.format(ff1.v1))
print('_v = {} \n'.format(ff1._v))
# print(ff1.get_v())
# print(ff1.change_v())
print()


print('is positive:', ff1.__class__.__name__)
for n in ff1._v:
    # print(n)
    print('{}\t{}'.format(n, ff1.is_positive(n)))
print()

print('is positive:', ff1.__class__.__name__)
for n in ff1.v1:
    # print(n)
    print('{}\t{}'.format(n, ff1.is_positive(n)))
print()

ff1.change_v()

print('is positive:', ff1.__class__.__name__)
for n in ff1.v1:
    # print(n)
    print('{}\t{}'.format(n, ff1.is_positive(n)))
print()



positive_l = list(ff1.filter_ints()) 
negative_l = list(ff1.filter_ints_n()) 
print('positive list: {}'.format(positive_l))  
print('negative list: {}'.format(negative_l))  



print('\n' + '=' * 94) 



# ===========================================================




print('=' * 94 + '\n') 
print('\t\t\ttests/test_ch7/test_filter_funcs.py\n')

from unittest import TestCase # 1
from unittest.mock import patch, call # 2
from nose.tools import assert_equal # 3
from ch7.filter_funcs import filter_ints # 4

class FilterIntsTestCase(TestCase): # 5
    @patch('ch7.filter_funcs.is_positive') # 6
    def test_filter_ints(self, is_positive_mock): # 7
        # preparation
        v = [3, -4, 0, 5, 8]
        # execution
        filter_ints(v) # 8
        # verification
        assert_equal([call(3), call(-4), call(0), call(5), call(8)], is_positive_mock.call_args_list) # 9


print('\n' + '=' * 94) 



# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""

