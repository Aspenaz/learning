
#! [Alert: Deprecated method, do not use]  
#? [Query or question: Should this method be exposed in the public API?]  
#// [CommentedOut: Do not use] 
#todo [Refactor: this method so that it conforms to the API. Create some test cases]   
#* [Important: information is highlighted] 


# ===========================================================
#               Improve readability
# ===========================================================


""" print('=' * 80 + '\n') 
print('\t\t\tdata.science.example.py\n')

def do_report(data_source):
    data = fetch_data(data_source)
    parsed_data = parse_data(data)
    filtered_data = filter_data(parsed_data)
    polished_data = polish_data(filtered_data)

    final_data = analyse(polished_data)

    report = Report(final_data)
    return report 


print()

   
print('\n' + '=' * 80)  """

#==========================================================

print('=' * 80 + '\n') 
print('\t\t\t matrix.multiplication.nofunc.py\n')

a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]

c = [[sum(i * j for i, j in zip(r, c)) for r in a] for c in zip(*b)]  # c: [[9, 23], [3, 7]]  # Respuesta incorrecta.
print('c:', c)
print()

c = [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]  # c: [[9, 3], [23, 7]]
print('c:', c)  # c: [[9, 3], [23, 7]]
print()

'c in zip(*b) = [(5, 2), (1, 1)]'
'r in a       = [[1, 2], [3, 4]]'
'i * j for i, j in zip(r, c) = '
'zip(r, c) = [  [ [1, 2]i x (5, 2)j, [1, 2]i x (1, 1)j ],  [ [3, 4]i x(5, 2)j, [3, 4]i x (1, 1)j ]  ]'

print('\n' + '=' * 80) 

#==========================================================

print(list(zip('abcdefg', range(3), range(4))))  # [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
print()
print(list(zip(a, b)))  # [ ([1, 2], [5, 1]), ([3, 4], [2, 1]) ]
print()
print(list(zip(a, *b)))  # [ ([1, 2], 5, 2), ([3, 4], 1, 1) ]   
print()
print(list(zip(b)))  # [([5, 1],), ([2, 1],)]
print()
print(list(zip(*b)))  # [(5, 2), (1, 1)]
print()
print(list(zip(r, c) for c in zip(*b) for r in a))
print()
r = [[1, 2], [3, 4]]
c = [(5, 2), (1, 1)]
print(list(zip(r, c)))  # [ ([1, 2], (5, 2)), ([3, 4], (1, 1)) ]



#==========================================================

print('=' * 80 + '\n') 
print('\t\t\t matrix.multiplication.func.py\n')

def matrix_mul(a, b):
    return  [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]

a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]

c = matrix_mul(a, b)
print('c:', c)  # c: [[9, 3], [23, 7]] 


print('\n' + '=' * 80) 



# ===========================================================
#               Improve traceability
# ===========================================================


print('=' * 80 + '\n') 
print('\t\t\t vat.py\n')

price = 100 
final_price1 = price * 1.2 
final_price2 = price + price / 5.0
final_price3 = price * (100 + 20) / 100.0 
final_price4 = price + price * 0.2 

print('final_price1:', final_price1)
print('final_price2:', final_price2)
print('final_price3:', final_price3)
print('final_price4:', final_price4)



print('\n' + '=' * 80) 

#==========================================================


print('=' * 80 + '\n') 
print('\t\t\t vat.function.py\n')

print() 

def calculate_price_with_vat(price, vat):
    return price * (100 + vat) / 100


final_price = calculate_price_with_vat(100, 20)
print (final_price)  # 120.0

print()



print('\n' + '=' * 80) 



# ===========================================================
#               Scopes and name resolution
# ===========================================================


print('=' * 80 + '\n') 
print('\t\t\t scoping.level.1.py\n')

test = 0  # this is defined in the global scope

def my_fuction():
    test = 1  # # this is defined in the local scope of the function 
    print('my_function:', test)

my_fuction()
print('global:', test)


print('\n' + '=' * 80) 


#==========================================================

print('=' * 80 + '\n') 
print('\t\t\t scoping.level.2.py\n')


test = 0  # global scope 

def outer():
    test = 1  # outer scope

    def inner():
        test = 2  # inner scope 
        print('inner:', test)

    inner()
    print('outer:', test)


outer()
print('global:', test)
# inner: 2
# outer: 1
# global: 0


print('\n' + '=' * 80) 



# ===========================================================
#           The global and nonlocal statements
# ===========================================================

print('=' * 80 + '\n') 
print('\t\t\t scoping.level.2.nonlocal.py\n')

test = 0                    # global scope 

def outer():
    test = 1                # outer scope 

    def inner():
        nonlocal test 
        test = 2            # nearest enclosing scope 
        print('inner:', test)
        
    inner()
    print('outer:', test)   # 2 by nonlocal


outer()
print('global:', test) 

# inner: 2
# outer: 2
# global: 0



print('\n' + '=' * 80) 

#==========================================================

print('=' * 80 + '\n') 
print('\t\t\t scoping.level.2.nonlocal.py modified by global.1\n')

test = 0                # global scope 

def outer():
    test = 1            # outer scope 

    def inner():
        global test     # outer scope 
        test = 2
        print('inner:', test)

    inner()
    print('outer:', test)


outer()
print('global:', test) 

# inner: 2
# outer: 1
# global: 2


print('\n' + '=' * 80) 

#==========================================================

print('=' * 80 + '\n') 
print('\t\t\t scoping.level.2.nonlocal.py modified by global.2\n')

def outer():
    def inner():
        global test  # global scope 
        test = 2
        print('inner:', test)

    inner()
    print('outer:', test)


outer()
print('global:', test) 

# inner: 2
# outer: 2
# global: 2


print('\n' + '=' * 80) 

#==========================================================


print('=' * 80 + '\n') 
print('\t\t\t scoping.level.2.global.py\n')

test = 0            # global scope 

def outer():
    test = 1        # outer scope 

    def inner():
        global test 
        test = 2    # global scope 
        print('inner:', test)
        
    inner()
    print('outer:', test)


outer()
print('global:', test)

# inner: 2
# outer: 1
# global: 2


print('\n' + '=' * 80) 


# ===========================================================
#   Assignment to argument names don't affect the caller
# ===========================================================

print('=' * 80 + '\n') 
print('\t\t\t key.points.assignment.py\n')

x = 3

def func(x):
    x = 7 
    print(x)
    

func(x)     # 7
print(x)    # 3


print('\n' + '=' * 80) 

# ===========================================================
#           Changing a mutable affects the caller
# ===========================================================

print('=' * 80 + '\n') 
print('\t\t\t key.points.mutable.py\n')


x = [1, 2, 3]

def func(x):
    x[1] = 42 


print(x)  # [1, 2, 3]   
func(x)   # this caller change to the list!
print(x)  # [1, 42, 3]


print('\n' + '=' * 80) 

#==========================================================


print('=' * 80 + '\n') 
print('\t\t\t key.points.mutable.assignment.py\n')

x = [1, 2, 3]

def func(x):
    x[1] = 42               # this changes the caller!
    x = 'something else'    # this points x to a new string object 


print(x)                    # [1, 2, 3]   
func(x)   
print(x)                    # [1, 42, 3] 
# print(func.x)             #! how I can have access to variable x through func() method? 
# print()


print('\n' + '=' * 80) 

#==========================================================

print('=' * 80 + '\n') 


class Func_x:
    x = [1, 2, 3]

    def func(x):
        x[1] = 42               # this changes the caller!
        x = 'something else'    # this points x to a new string object 


print(Func_x.x)                 # [1, 2, 3]   
Func_x.func(Func_x.x)   
print(Func_x.x)                 # [1, 42, 3] 
# print(Func_x.func.x)          #! Extract innner scope variable!!!!!!!! How is it?   # AttributeError: 'function' object has no attribute 'x'
print()

f = Func_x()
print('x=', f.x)
# print('x in fun()=', f.func.x)  #! how I can have access to variable x through func() method? 


print('\n' + '=' * 80) 


# ===========================================================
"""           How to specify input parameters             """
# ===========================================================
""" There are five different ways of specifying input parameters. Let's look at them one
by one. """


#! [Alert: Deprecated method, do not use]  
#? [Query or question: Should this method be exposed in the public API?]  
#// [CommentedOut: Do not use] 
#todo [Refactor: this method so that it conforms to the API. Create some test cases]   
#* [Important: information is highlighted] 


print('=' * 80 + '\n') 
print('\t\t\t .py\n')



print('\n' + '=' * 80) 
 
 #==========================================================

 #==========================================================


print('=' * 80 + '\n') 
print('\t\t\t .py\n')



print('\n' + '=' * 80) 


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\t .py\n')



print('\n' + '=' * 80) 


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\t .py\n')



print('\n' + '=' * 80) 


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\t .py\n')



print('\n' + '=' * 80) 



 
#================arguments.keyword.py========================
""" 
print() 

# def func(a, b, c):
def func(a=1, b=2, c=3):
    print(a, b, c)

#func(a=1, b=2, c=3)
func()
func(4, 5, 6)


print() 

"""
#================arguments.default.py========================
""" 
print() 

def func(a, b=4, c=88):
    print(a, b, c)

func(1)
func(b=5, a=7, c=9)
func(42, c=9)

print() 

"""

#================arguments.variable.positional.py========================
""" 
print() 

def minimum(*n):
    #print(n)
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value 
        print(mn)
        
minimum(1, 3, -7, 9)
minimum()

print() 

"""

#================arguments.variable.positional.unpacking.py========================
""" 
print() 

def func(*args):
    print(args)

values = (1, 3, -7, 9)
func(values)
func(*values)

print()

"""

#================arguments.variable.keyword.py========================
""" 
print() 

def func(**kwargs):
    print(kwargs)

func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))    

print()

"""

#================arguments.variable.db.py========================
""" 
print() 

def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)


connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='fab', pwd='gandalf')

print()

 """
 #================arguments.keyword.only.py========================
""" 
print() 

def kwo(*a, c):
    print(a, c)

kwo(1, 2, 3, c=7)
kwo(c=4)

print()

def kwo2(a, b=42, *, c):
    print(a, b, c)

kwo2(3, b=7, c=99)
kwo2(3, c=13)

print()
"""

#================arguments.all.py========================
""" 
print() 

def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs) 

func(1, 2, 3, *(4, 5, 6), **{'A': 'a', 'B': 'b'})
print()
func(7, 8, 9, 10, 11, 12, 13, 14, C='c', D='d', E='e')     

print() 
"""

#================arguments.all.kwonly.py========================
""" 
print() 

def func_with_kwonly(a, b=42, *args, c, d=256, **kwargs):
    print('a, b:', a, b)
    print('c, d:', c, d)
    print('args:', args)
    print('kwargs:', kwargs)
    
func_with_kwonly(3, 43, c=0, d=1, *(7, 9, 11), e='E', f='F')
print()
func_with_kwonly(3,  c=0, *(7, 9, 11), e='E', f='F')
print()
func_with_kwonly(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F')

print() 
"""

#================arguments.defaults.mutable.py========================
""" 
print() 

def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    print(len(a))
    a.append(len(a))
    print(a)
    print(len(a))
    b[len(a)] = len(a)

func() ; print() 
func() ; print() 
func() ; print() 

print() 
 """
#================arguments.defaults.mutable.intermediate.call.py========================

print() 
""" 
def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    print(len(a))
    a.append(len(a))
    print(a)
    print(len(a))
    b[len(a)] = len(a)
    print(b)

func() ; print() 
func(a=[1, 2, 3], b={'B': 1}) ; print() 
func() ; print() 

print() 
"""
#================arguments.defaults.mutable.no.trap.py========================
""" 
print() 

def func (a=None):
    if a is None:
        a = []
    #print(a)
    return a
        
#func()
#func([1, 2, 3])

x = func()
print(x)
y = func([1, 2, 3])
print(y)

print() 
"""

#================return.single.value.py========================
""" 
print() 

def factorial(n):
    if n in (0, 1):
        return 1
    result = n 
    print('n =', n, '\n')
    for k in range(2, n):
        print('result =', result)
        print('k =', k)
        print('result = result * k |', result, '=', result, '*', k)
       # print(result, '=', result, '*', k)
        result *= k 
        print('result =', result)
        print()
    return result 

f5 = factorial(5)
print(f5)

print() 
"""

#================return.single.value.2.py========================
""" 
print() 

from functools import reduce 
from operator import mul 

def factorial (n):
    return reduce (mul, range(1, n + 1), 1)

f5 = factorial(5)
print(f5)
f7 = factorial(7)
print(f7)

print() 

"""

#================return.multiple.py========================
""" 
print() 

def moddiv(a, b):
    return a // b, a % b 

print(moddiv(20, 7))   # (2, 6)

print() 
 """

#================recursive.factorial.py========================
""" 
print() 

def factorial(n):
    if n in (0, 1):
        return 1
    return factorial(n - 1) * n

f5 = factorial(5)
print(f5)
f7 = factorial(7)
print(f7)

print() 
 """
#================filter.regular.py========================
""" 
print() 

def is_multiple_of_five(n):
    return not n % 5
def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n + 1)))

print(get_multiples_of_five(50))
print()

m5 = is_multiple_of_five(15)
print(m5)

m5 = is_multiple_of_five(17)
print(m5)

print() 
 """


#================lambda.explained.py========================
'''

print('=' * 80 + '\n') 

# Example 1: adder
def adder(a, b):
    return a + b 

print(adder(4, 3))

# Example 1 is equivalent to:
adder_lambda = lambda a, b: a + b
print(adder_lambda(3, 3))

print() 

# Example 2: to uppercase
def to_upper(s):
    return s.upper()

print(to_upper('Upper Case'))

# Example 2 is equivalent to:
to_upper_lambda = lambda s: s.upper()
print(to_upper_lambda('Upper Case Lambda'))

print('\n' + '=' * 80) 

#================filter.lambda.py========================

print('=' * 80 + '\n') 

def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n + 1)))

print(get_multiples_of_five(50))


print('\n' + '=' * 80) 


'''




#================func.attributes.py========================
""" 
print('=' * 80 + '\n') 

def multiplication(a, b=1):
    return a * b 

print(multiplication(3))
print(multiplication(3, 4))
print()

special_attributes = [
    '_doc_', '_name_', '_qualname_', '_module_',
    '_defaults_', '_code_', '_globals_', '_dict_',
    '_closure_', '_annotations_', '_kwdefaults_',
]

for attribute in special_attributes:
    print(attribute)
   # print(attribute, '->', getattr(multiplication, attribute))

print('\n' + '=' * 80) 
  """





#================primes.py========================

print('=' * 80 + '\n') 

from math import sqrt, ceil 

def get_primes(n):
    primelist = []
    for candidate in range(2, n + 1):
        print('primelist:', primelist, len(primelist))
        print('candidate:', candidate)
        is_prime = True 
        root = int(ceil(sqrt(candidate)))
        print('sqrt(candidate):', sqrt(candidate))
        print('ceil(sqrt(candidate)):', ceil(sqrt(candidate)))
        print('root:', root)
        for prime in primelist:
            print('prime in primelist:', prime)
            if prime > root:
                print('prime > root:', prime, '>', root, ' = True')
                break 
            if candidate % prime == 0:
                print('candidate % prime:', candidate, '%', prime, '=', candidate % prime)
                is_prime = False 
                print('is Prime =', is_prime)
                break 
        if is_prime:
            print(candidate, 'is Prime')
            primelist.append(candidate)
        print()
    return primelist

print(get_primes(11))


print('\n' + '=' * 80) 

 

 
 
""" 
#================.py========================

print('=' * 80 + '\n') 

print('\n' + '=' * 80) 
 """
 
 
 
 
 
""" 
#================.py========================

print('=' * 80 + '\n') 

print('\n' + '=' * 80) 
 """
