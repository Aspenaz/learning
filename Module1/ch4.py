#
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



#! [Alert: Deprecated method, do not use]  
#? [Query or question: Should this method be exposed in the public API?]  
#// [CommentedOut: Do not use] 
#todo [Refactor: this method so that it conforms to the API. Create some test cases]   
#* [Important: information is highlighted] 




# ===========================================================
"""           How to specify input parameters             """
# ===========================================================
""" There are five different ways of specifying input parameters. """



# ===========================================================
#                 Positional arguments
# ===========================================================

print('=' * 80 + '\n') 
print('\t\t\t arguments.positional.py\n')


def func(a, b, c):
    print(a, b, c)
    
func(1, 2, 3)


print('\n' + '=' * 80) 

# ===========================================================
#           Keyword arguments and default values
# ===========================================================
""" Keyword arguments are assigned by keyword using the name=value syntax """

print('=' * 80 + '\n') 
print('\t\t\t arguments.keyword.py\n')


def func(a, b, c):
    print(a, b, c)

func(a=1, b=2, c=3)
func()
func(4, 5, 6)


print('\n' + '=' * 80) 
 
#==========================================================

print('=' * 80 + '\n') 
print('\t\t\t arguments.default.py\n')


def func(a, b=4, c=88):
    print(a, b, c)

func(1)
func(b=5, a=7, c=9)
func(42, c=9)


print('\n' + '=' * 80) 


# ===========================================================
#             Variable positional arguments
# ===========================================================


print('=' * 80 + '\n') 
print('\t\t\t arguments.variable.positional.py\n')


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


print('\n' + '=' * 80) 

#==========================================================

print('=' * 80 + '\n') 
print('\t\t\t arguments.variable.positional.unpacking.py\n')


def func(*args):
    print(args)

values = (1, 3, -7, 9)
func(values)                # equivalent to: func((1, 3, -7, 9))
func(*values)               # equivalent to: func(1, 3, -7, 9)


print('\n' + '=' * 80) 


# ===========================================================
#             Variable keyword arguments
# ===========================================================
 

print('=' * 80 + '\n') 
print('\t\t\t arguments.variable.keyword.py\n')


def func(**kwargs):
    print(kwargs)

# All calls equivalent. They print: {'a': 1, 'b': 42}
func(a=1, b=42)
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))    


print('\n' + '=' * 80) 

#==========================================================

print('=' * 80 + '\n') 
print('\t\t\t arguments.variable.db.py\n')


def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)
    # we then connect to the db (commented out)
    # db.connect(**conn_params)

connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='fab', pwd='gandalf')


print('\n' + '=' * 80) 


# ===========================================================
#                 Keyword-only arguments
# ===========================================================

print('=' * 80 + '\n') 
print('\t\t\t arguments.keyword.only.py\n')


def kwo(*a, c):             #* variable positional arguments (*name, or simply *)
    print(a, c)

kwo(1, 2, 3, c=7)           # prints: (1, 2, 3) 7
kwo(c=4)                    # prints: () 4
# kwo(1, 2) # breaks, invalid syntax, with the following error
# TypeError: kwo() missing 1 required keyword-only argument: 'c'

def kwo2(a, b=42, *, c):    #* variable positional arguments (*name, or simply *)
    print(a, b, c)
    
print()
kwo2(3, b=7, c=99)          # prints: 3 7 99
kwo2(3, c=13)               # prints: 3 42 13
# kwo2(3, 23) # breaks, invalid syntax, with the following error
# TypeError: kwo2() missing 1 required keyword-only argument: 'c'


print('\n' + '=' * 80) 



# ===========================================================
"""               Combining input parameters              """
# ===========================================================
""" You can combine input parameters, as long as you follow these ordering rules:
• When defining a function, normal positional arguments come first (name),
then any default arguments (name=value), then the variable positional
arguments (*name, or simply *), then any keyword-only arguments (either
name or name=value form is good), then any variable keyword arguments
(**name).
• On the other hand, when calling a function, arguments must be given in the
following order: positional arguments first (value), then any combination of
keyword arguments (name=value), variable positional arguments (*name),
then variable keyword arguments (**name). """


#==========================================================

print('=' * 80 + '\n') 
print('\t\t\t arguments.all.py\n')


def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs) 

func(1, 2, 3, *(4, 5, 6), **{'A': 'a', 'B': 'b'})
print()
func(7, 8, 9, 10, 11, 12, 13, 14, C='c', D='d', E='e')  


print('\n' + '=' * 80) 
 
#==========================================================

print('=' * 80 + '\n') 
print('\t\t\t arguments.all.kwonly.py\n')


def func_with_kwonly(a, b=42, *args, c, d=256, **kwargs):
    print('a, b:', a, b)
    print('c, d:', c, d)
    print('args:', args)
    print('kwargs:', kwargs)
    
func_with_kwonly(3, 41, c=0, d=1, *(7, 9, 11), e='E', f='F')    ; print()
func_with_kwonly(3,  c=0, *(7, 9, 11), g='G', h='H')            ; print()
func_with_kwonly(3, 43, *(7, 9, 11), c=0, d=1, i='I', j='J')    ; print() 


print('\n' + '=' * 80) 


# ===========================================================
#*            Avoid the trap! Mutable defaults
# ===========================================================


print('=' * 80 + '\n') 
print('\t\t\t arguments.defaults.mutable.py\n')


def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    print(len(a))
    a.append(len(a))      # this will affect a's default value
    print(a)
    print(len(a))
    b[len(a)] = len(a)    # and this will affect b's one

func()          ; print() 
func()          ; print() 
func()          ; print() 


print('\n' + '=' * 80) 
 
#=========================================================

print('=' * 80 + '\n') 
print('\t\t\t arguments.defaults.mutable.intermediate.call.py\n')


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

func()                          ; print() 
func(a=[1, 2, 3], b={'B': 1})   ; print() 
func() 


print('\n' + '=' * 80) 
 
#=========================================================

print('=' * 80 + '\n') 
print('\t\t\t arguments.defaults.mutable.no.trap.py\n')


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


print('\n' + '=' * 80) 



# ===========================================================
"""                  Return values                        """
# ===========================================================
""" Functions are usually allowed to return one object
    (one value) but, in Python, you can return a tuple, 
    and this implies that you can return whatever you want.  """
 
#=========================================================

print('=' * 80 + '\n') 
print('\t\t\t return.none.py\n')


def func():
    pass

func()          # the return of this call won't be collected. It's lost.
a = func()      # the return of this one instead is collected into `a`
print(a)        # prints: None


print('\n' + '=' * 80) 
 
#=========================================================

print('=' * 80 + '\n') 
print('\t\t\t return.single.value.py\n')


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


print('\n' + '=' * 80) 
 
#=========================================================

print('=' * 80 + '\n') 
print('\t\t\t return.single.value.2.py\n')


from functools import reduce 
from operator import mul 

def factorial (n):
    return reduce (mul, range(1, n + 1), 1)

f5 = factorial(5)
print(f5)
f7 = factorial(7)
print(f7)


print('\n' + '=' * 80) 

# ===========================================================
"""              Returning multiple values                """
# ===========================================================
""" To return multiple values is very easy, you just use tuples 
(either explicitly or implicitly). """



#=========================================================

print('=' * 80 + '\n') 
print('\t\t\t return.multiple.py\n')


def moddiv(a, b):
    return a // b, a % b 

print(moddiv(20, 7))            # (2, 6)


print('\n' + '=' * 80) 


# ===========================================================
"""                  A few useful tips                    """
# ===========================================================
""" When writing functions, it's very useful to follow guidelines so 
    that you write them well. I'll quickly point some of them out here: 

• Functions should do one thing: Functions that do one thing are easy to
  describe in one short sentence. Functions which do multiple things can be
  split into smaller functions which do one thing. These smaller functions are
  usually easier to read and understand. Remember the data science example
  we saw a few pages ago.
  
• Functions should be small: The smaller they are, the easier it is to test them
  and to write them so that they do one thing.
  
• The fewer input parameters, the better: Functions which take a lot of
  arguments quickly become harder to manage (among other issues).
  
• Functions should be consistent in their return values: Returning False
  or None is not the same thing, even if within a Boolean context they both
  evaluate to False. False means that we have information (False), while
  None means that there is no information. Try writing functions which return
  in a consistent way, no matter what happens in their body.
  
• Functions shouldn't have side effects: In other words, functions should not
  affect the values you call them with. This is probably the hardest statement
  to understand at this point. """




# ===========================================================
#*                  Recursive functions
# ===========================================================

print('=' * 80 + '\n') 
print('\t\t\t recursive.factorial.py\n')


def factorial(n):
    if n in (0, 1):
        return 1
    return factorial(n - 1) * n

f5 = factorial(5)
print(f5)
f7 = factorial(7)
print(f7)


print('\n' + '=' * 80) 

# ===========================================================
#*                  Anonymous functions
# ===========================================================

print('=' * 80 + '\n') 
print('\t\t\t filter.regular.py\n')


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


print('\n' + '=' * 80) 
 
#=========================================================

print('=' * 80 + '\n') 
print('\t\t\t filter.lambda.py\n')


def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n + 1)))

print(get_multiples_of_five(50))


print('\n' + '=' * 80) 

#=========================================================

print('=' * 80 + '\n') 
print('\t\t\t lambda.explained.py\n')


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

# ===========================================================
#*                 Function attributes
# ===========================================================

print('=' * 80 + '\n') 
print('\t\t\t func.attributes.py\n')


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

# ===========================================================
""" #                 Built-in functions                  """
# ===========================================================
""" They are available anywhere and you can get a list of them by inspecting 
the builtins module with dir(__builtins__). Some of them we've already seen, 
such as any, bin, bool, divmod, filter, float, getattr, id, int, len, list, 
min, print, set, tuple, type, and zip, but there are many more,  """




# ===========================================================
#*                  Final example
# ===========================================================


print('=' * 80 + '\n') 
print('\t\t\t rimes.py\n')


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



# ===========================================================
"""#*               Documenting your code                 """
# ===========================================================
""" You can find the guidelines for documenting Python in PEP257 - Docstring conventions. 
    Sphinx is probably the most widely used tool for creating Python documentation. """
 
 
print('=' * 80 + '\n') 
print('\t\t\t docstrings.py\n')

def square(n):
    """Return the square of a number n. """
    return n ** 2

def get_username(userid):
    """Return the username of a user given their id. """
    return db.get(user_id=userid).username


print('\n' + '=' * 80) 

#=========================================================

print('=' * 80 + '\n') 
print('\t\t\t docstrings.py\n')

def connect(host, port, user, password):
    """Connect to a database.
    Connect to a PostgreSQL database directly, using the given
    parameters.
    
    :param host: The host IP.
    :param port: The desired port.
    :param user: The connection username.
    :param password: The connection password.
    :return: The connection object.
    """

    # body of the function here...
    
    #* return connection 


print('\n' + '=' * 80) 


# ===========================================================
"""#*                Importing objects                    """
# ===========================================================
"""There are many different ways to import objects into a namespace, but the most common 
ones are just two: import module_name and from module_name import function_name. 

Both forms have the option to change the name of the imported object using the
as clause, like this:

from mymodule import myfunc as better_named_func
"""

print('=' * 80 + '\n') 
print('\t\t\t karma/test_nt.py\n')


import unittest                         # imports the unittest module
from math import sqrt                   # imports one function from math
from random import randint, sample      # two imports at once

from mock import patch
from nose.tools import (                # multiline import
    assert_equal,
    assert_list_equal,
    assert_not_in,
)

from karma import nt, utils                        


print('\n' + '=' * 80) 

#=========================================================

print('=' * 80 + '\n') 

""" 
Imagine that you have defined a couple of functions: square(n) and cube(n) in a
module, funcdef.py, which is in the lib folder. You want to use them in a couple of
modules which are at the same level of the lib folder, called func_import.py, and
func_from.py. Showing the tree structure of that project produces something like this:

├── func_from.py
├── func_import.py
├── lib
    ├── funcdef.py
    └── __init__.py
 """
 
print('\t\t\t funcdef.py\n')

def square(n):
    return n ** 2

def cube(n):
    return n ** 3


 
print('\n' + '=' * 80 + '\n') 



print('\t\t\t func_import.py\n')

import lib.funcdef
print(lib.funcdef.square(10))
print(lib.funcdef.cube(10))



print('\n' + '=' * 80 + '\n') 



print('\t\t\t func_from.py\n')

from lib.funcdef import square, cube
print(square(10))
print(cube(10))



print('\n' + '=' * 80) 


# ===========================================================
"""#*                Relative imports                    """
# ===========================================================
""" For a complete explanation of relative imports, refer to PEP328
(https://www.python.org/dev/peps/pep-0328) """

# from .mymodule import myfunc




#=========================================================

print('=' * 80 + '\n') 
print('\t\t\t .py\n')




print('\n' + '=' * 80) 

#=========================================================