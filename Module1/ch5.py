
# ===========================================================
#                          map
# ===========================================================

"""

print('=' * 80 + '\n') 
print('\t\t\tdecorate.sort.undecorate.py.py\n')

students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]
 
def decorate(student):
    return (sum(student['credits'].values()), student)

def undecorate0(decorated_student):
    return decorated_student[0]

def undecorate1(decorated_student):
    return decorated_student[1]

students = sorted(map(decorate, students), reverse=True)
for student in students:
    print(student)
print()   

students0 = list(map(undecorate0, students))
for student in students0:
    print(student)
print()
    
students1 = list(map(undecorate1, students))    
for student in students1:
    print(student)
    
print()

   
print('\n' + '=' * 80) 



"""

# ===========================================================
#                          zip
# ===========================================================

"""

print('\t\t\tzip.grades.py\n')
print('=' * 80 + '\n') 

grades = [18, 23, 30, 27, 15, 9, 22]
avgs = [22, 21, 29, 24, 18, 18, 24]

zip_avg_grades = list(zip(avgs, grades))
print(zip_avg_grades)

lambda_avg_grades = list(map(lambda *a: a, avgs, grades))
print(lambda_avg_grades)

print()

students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

def decorate(students):
    return (students['id'], students['credits'], sum(students['credits'].values()))

dstudents = sorted(map(decorate, students), reverse=False)

for student in dstudents:
    print(student)
print()

print('id   credits')
for student in dstudents:
    print(student[0], '    ', student[2])
    
print('\n' + '=' * 80) 


#==========================================================


print('\t\t\tmaxims.py\n')
print('=' * 80 + '\n') 

a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]

maxs = map(lambda n: max(*n), zip(a, b, c))
print(list(maxs))

print('\n' + '=' * 80) 


"""

# ===========================================================
#                       filter
# ===========================================================

"""

print('\t\t\tfilter.py\n')
print('=' * 80 + '\n')  

test = [2, 5, 8, 0, 0, 1, 0]
list_none = list(filter(None, test))
print(list_none)

list_filter_1 = list(filter(lambda x: x, test))
print(list_filter_1)

list_filter_2 = list(filter(lambda x: x > 4, test))
print(list_filter_2)

print('\n' + '=' * 80) 


"""

# ===========================================================
#                     Comprehensions
# ===========================================================

"""

print('\t\t\tsquares.map.py\n')
print('=' * 80 + '\n')  

squares = []
for n in range(10):
    squares.append(n ** 2)
    #print(squares)
print(squares)

print()

squares2 = []
squares2 = map(lambda n: n**2, range(10))
print(list(squares2))

print()

squares3 = []
squares3 = map(lambda n: n*3, squares)
print(list(squares3))


print('\n' + '=' * 80) 


#===========================================================


print('\t\t\teven.squares.py\n')
print('=' * 80 + '\n') 

#sq1 = list(filter(lambda n: not n % 2, map(lambda n: n ** 2, range(10))))
sq1 = list(filter(lambda n: not n % 2, map(lambda n: n ** 2, range(11))))

sq2 = [n ** 2 for n in range(10) if not n % 2]  # if not n % 2: Si el residuo es cero.

sq3 = [n ** 2 for n in range(10) if n % 2]  # if n % 2: Si el residuo es distinto de cero.

print(9%2, '    ', 9//2)
print(not 9%2, '    ', not 8%2)
print(sq1)
print(sq2)
print(sq3)
print(sq1 == sq2)

print('\n' + '=' * 80) 


  
"""

# ===========================================================
#                  Nested comprehensions
# ===========================================================

""" 

print('\t\t\tpairs.for.loop.py\n')
print('=' * 80 + '\n') 

items = 'ABCDE'
print('tems:', items)
print('len(items):', len(items))
pairs = []
for a in range(len(items)):
    print('a:', a)
    for b in range(a, len(items)):
        print(b, items[a], items[b])
        pairs.append((items[a], items[b]))
    print()

print(pairs)

print('\n' + '=' * 80) 


items2 = 'ABCDE'
pairs2 = []
for a in range(len(items2)):
    for b in range(len(items2)):
        pairs2.append((items2[a], items2[b]))
 
print()
print(pairs2) 
 
print('\n' + '=' * 80) 


#===========================================================


print('\t\t\tpairs.list.comprehension.py\n')
print('=' * 80 + '\n') 

items = 'ABCDE'
pairs = [(items[a], items[b]) for a in range(len(items)) for b in range(a, len(items))]
print(pairs)

print('\n' + '=' * 80) 


"""

# ===========================================================
#                 Filtering a comprehension
# ===========================================================

""" 

print('=' * 80 + '\n') 
print('\t\t\tpythagorean.triple.py\n')

from math import sqrt 

mx = 10 
legs = [(a, b, sqrt(a**2 + b**2)) for a in range(1, mx) for b in range(a, mx)]
i = 1
for leg in legs:
#    print(i, leg, '  ', leg[2])
    i += 1
print()

legs_f1 = list(filter(lambda triple: triple[2].is_integer(), legs))
print('legs_f1:', legs_f1)
print()

legs_f2 = [(a, b, int(c)) for a, b, c in legs_f1]
print('legs_f2:', legs_f2)
print()

# legs_f2 = list(filter(lambda triple: triple[2], legs))
# print(legs_f2)


print('\n' + '=' * 80) 

 
#===========================================================


print('=' * 80 + '\n') 
print('\t\t\tpythagorean.triple.int.py\n') 

from math import sqrt

mx = 10
legs = [(a, b, sqrt(a**2 + b**2)) for a in range(1, mx) for b in range(a, mx)]
legs = filter(lambda triple: triple[2].is_integer(), legs)
print('1. ', legs)
legs = list(map(lambda triple: triple[:2] + (int(triple[2]), ), legs))
print('2. ', legs)


print()
list_n = [1, 2, 3, 4, 5, 6, 7]
print(list_n[:2])

print('\n' + '=' * 80) 


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\tpythagorean.triple.comprehension.py\n')

from math import sqrt 

mx = 10
legs = [(a, b, sqrt(a**2 + b**2)) for a in range(1, mx) for b in range(a, mx)]
legs = [(a, b, int(c)) for a, b, c in legs if c.is_integer()]
print(legs)


print('\n' + '=' * 80) 


"""

# ===========================================================
#                   dict comprehensions
# ===========================================================

"""

print('=' * 80 + '\n') 
print('\t\t\tdictionary.comprehensions.py\n')

from string import ascii_lowercase 
import pprint

print(ascii_lowercase)
print()

lettermap_list = list((c, k) for k, c in enumerate(ascii_lowercase, 1))
print(lettermap_list)
print()

lettermap_dict = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
print(lettermap_dict)
print()

lettermap = {c:k for k, c in enumerate(ascii_lowercase, 1)}
print(lettermap)
pprint.pprint(lettermap)

# for key, value in lettermap2.items():
#     print(key, ':', value)
print()

print('\n' + '=' * 80) 


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\tdictionary.comprehension.duplicates.py\n')

word = 'World'
swaps = {c: c.swapcase() for c in word}
print(swaps)

print('\n' + '=' * 80) 
 

#==========================================================


print('=' * 80 + '\n') 
print('\t\t\tdictionary.comprehension.positions.py\n')

word = 'World'
positions = {c:k for k, c in enumerate(word)}
print(positions); print()

position2 = {c:k for k, c in enumerate(word, 1)}
print(position2)

print('\n' + '=' * 80) 


"""

# ===========================================================
#                   set comprehensions
# ===========================================================

"""

print('=' * 80 + '\n') 
print('\t\t\tset.comprehensions.py\n')

word = 'World'

letters1 = set(c for c in word)
print(letters1)

letters2 = {c for c in word}
print(letters2)

print(letters1 == letters2)


print('\n' + '=' * 80) 

"""

# ===========================================================
#                   Generator Functions
# ===========================================================

"""

print('=' * 80 + '\n') 
print('\t\t\tfirst.n.squares.py\n')

def get_squares(n):
    return [x**2 for x in range(n)]

print(get_squares(10))


def get_squares_gen(n):
    for x in range(n):
        yield x ** 2 

print(list(get_squares_gen(10)))


print('\n' + '=' * 80) 


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\tfirst.n.squares.manual.py\n')

def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

squares = get_squares_gen(4)
#print(list(squares))
print(squares)
print(next(squares))    
print(next(squares))   
print(next(squares))   
#print(next(squares))   
print(next(squares))      


print('\n' + '=' * 80) 


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\tgen.yield.return.py\n')

def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q**k 
        if result <= 100000:
            yield result 
        else:
            return 
        k += 1      
        
for n in geometric_progression(2, 5):
    print(n)

print()

def geometric_progression_while(a, p): # Este método sobrepasa el límite de result. 
    k = 0
    result = 0
    while result <= 100000: 
        result = a * p**k
        yield result 
        k += 1
        
for n in geometric_progression_while(2, 5):
    print(n)
             

print('\n' + '=' * 80) 



"""

# ===========================================================
#                   Going beyond next
# ===========================================================

"""

print('=' * 80 + '\n') 
print('\t\t\tfirst.n.squares.manual.method.py\n')

def get_squares_gen(n):
    for x in range(n):
        yield x ** 2 
        
for n in get_squares_gen(3):  # De 0 a 2
    print(n)

print()
       
squares = get_squares_gen(3)  # De 0 a 2, al siguiente StopIteration 
print(squares)
#print(list(squares))
print(squares.__next__()) # 0
print(squares.__next__()) # 1
print(squares.__next__()) # 4
# print(squares.__next__()) # StopIteration
# print(squares.__next__())


print('\n' + '=' * 80) 


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\tgen.send.preparation.py\n')

def counter(start=0):
    n = start 
    while True:
        yield n
        n += 1 
        
c = counter()
print(next(c)) #0
print(next(c)) #1
print(next(c)) #2
print(next(c)) #3
print(next(c)) #4
print(next(c)) #5
print(next(c)) #6
print(next(c)) #7

print('\n' + '=' * 80) 


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\tgen.send.preparation.stop.py\n')

stop = False 
def counter(start=0):
    n = start 
    while not stop:
        print('stop:', stop, '    not stop:', not stop) #stop: False   not stop: True
        yield n 
        n += 1 
     
c = counter()
print(c)
print(next(c)) #0
print(next(c)) #1
print(next(c)) #2
print(next(c)) #3
stop = True    # not stop = not True = False
#print(next(c)) #StopIteration
# No se detiene hasta encontrar un stop = True

print('\n' + '=' * 80) 


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\tgen.send.py\n')

def counter(start=0):
    n = start 
    while True:
        print('n:', n)
        result = yield n  # yield imprime el valor de n, detiene la ejecución y regresa a la llamada del generador counter().
        print(n, type(result), result)  # next y send() retoman la ejecución del generador y setean result después de yield.
        if result == 'Q':
            break
        n += 1

# for n in counter(3):  # No se detiene hasta que result = 'Q'
#     print(n)

c = counter()
#print(list(c)) # <class 'NoneType'> None
#print(c)       # <generator object counter at 0x000001D480F40120
print(next(c))  # n: 0
                # 0
                
print(next(c))  # 0 <class 'NoneType'> None
                # n: 1
                # 1
                
print(c.send('Won!')) # 1 <class 'str'> Won!
                      # n: 2
                      # 2
                      
print((c.send('value'))) # 2 <class 'str'> value
                         # n: 3
                         # 3

print((c.send(123.3)))  # 3 <class 'float'> 123.3
                        # n: 4
                        # 4
                         
print(next(c))  # 4 <class 'NoneType'> None
                # n: 5
                # 5

# print(c.send('Q'))  # 5 <class 'str'> Q
                    # StopIteration  # break con result = 'Q'


print('\n' + '=' * 80)  


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\tgen.yield.for.py\n')

def print_squares(start, end):
    for n in range(start, end):
        yield n ** 2
        
for n in print_squares(2, 5):
    print(n)
print()

print(print_squares(2, 5))  # <generator object print_squares at 0x00000238DA288EB0>
print()

print(list(print_squares(2, 5)))
print()

squares_dict = dict((c, k) for k, c in enumerate(print_squares(2, 5), 1))
print(squares_dict)
print()

squares_dict2 = {c: k for k, c in enumerate(print_squares(5, 8), 1)}
print(squares_dict2)
print()


print('\n' + '=' * 80) 


#==========================================================


print('=' * 80 + '\n') 
print('\t\t\tgenerator.expressions.py\n')

cubes = [k**3 for k in range(10)]  # [] Crea una lista. Y No un generador.

print(cubes)
print('type:', type(cubes))
print()

# print(list(cubes))
# print()

for n in cubes:
    print(n)
print()

dict_1 = dict((c, k) for k, c in enumerate(cubes, 1)) # Forma incorrecta para numerar esta lista.
print('dict_1:', dict_1)
print()
print('dict_1:')
for n  in dict_1:
    print(n)
print()

import pprint
dict_2 = {c:k for c, k in enumerate(cubes, 1)} # Forma correcta para este diccionario. Values son los cubos.
print('dict_2:')
pprint.pprint(dict_2)           # pprint No funciona como en lettermap.
print()

from string import ascii_lowercase 
lettermap = {c:k for k, c in enumerate(ascii_lowercase, 1)}
print('lettermap:')
# pprint.pprint(lettermap)        # ¿Por qué pprint no funciona igual en dict_2?
print()



print('cubes_gen:')
cubes_gen = (k**3 for k in range(10)) # () Crea un generador. Y no una lista.
print(cubes_gen)
print('type:', type(cubes_gen))
v_cubes_gen = cubes_gen         # Sólo asigna la dirección de memoria, no el dato.
print(list(cubes_gen))          # Generador almacena temporal en memoria por cada llamada. 
print(list(cubes_gen))          # luego el espacio de memoria se vacía. Mejor reasignar a otra variable.
print(v_cubes_gen)
print(list(v_cubes_gen))
print()

cubes_gen = (k**3 for k in range(10))
v_cubes_gen = cubes_gen         # Funciona igual que anterior. Luego se borra dato de memoria
print(list(v_cubes_gen))
print(list(v_cubes_gen))
print()

print('dict_3:')
cubes_gen = (k**3 for k in range(10)) # () Crea un generador. Y no una lista.
dict_3 = {c:k for c, k in enumerate(cubes_gen)}
pprint.pprint(dict_3)           # pprint No funciona como en lettermap.
pprint.pprint(dict_3)
print()

print('dict_4:')
cubes_gen = (k**3 for k in range(10)) # () Crea un generador. Y no una lista.
dict_4 = dict((c, k) for c, k in enumerate(cubes_gen, 1))
print(dict_4)
print(dict_4)
d_dict_4 = dict_4
pprint.pprint(d_dict_4)
print(type(d_dict_4))           # El diccionario no se borra del espacio de memoria.


print('\n' + '=' * 80) 


"""


# ==========================================================


"""


print('=' * 80 + '\n') 
print('\t\t\tgen.map.py\n')

def adder(*n):
    return sum(n)

a = (2, 3, 5, 10)
b = (1, 4, 6, 7, 8)
c = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
d = list(zip(range(10), range(1, 11)))

print('a:', adder(*a))
print('b:', adder(*b))

# print('c:', adder(*c)) # unsupported operand type(s) for +: 'int' and 'tuple'. 
print('c:\r')                       # Adder() no suma entre tuplas, sólo lo que hay dentro de cada tupla.
for n in c:
    print(n)   
    
print('d:', d)
print('d2:')
for n in d:
    print(n)
print()


s1 = sum(map(lambda n: adder(*n), zip(range(10), range(1, 11))))
s2 = sum(adder(*n) for n in zip(range(10), range(11)))
# Cada zip produce una tupla de dos números, esa tupla ingresa en adder(), 
# los dos números son sumados entre si y el resultado es sumado al siguente 
# por medio de sum().

print('s1:', s1)
print('s2:', s2)
print()

print('zip():', zip(range(10), range(1, 11)))
print()

print('zip():', (zip(range(10), range(1, 11))))
print()

print('list(zip())_1:', list(zip(range(10), range(1, 11))))
print('list(zip())_2:', list(zip(range(10), range(11))))
print()

dict_zip1 = {c:k for c, k in enumerate((zip(range(10), range(1, 11))), 1)}
print('dict_zip:', dict_zip1)
print()

import pprint
print('dict_zip:')
pprint.pprint(dict_zip1)    # pprint aquí sí funciona porque no es sobre un generador.
print()



#==========================================================



print()
print('\t\t\tPráctica\n')

def adder2(*n):
    return sum(n)

s3 = sum(map(lambda n: adder2(*n), zip(range(10), range(1, 11))))
s4 = sum(adder2(*n) for n in zip(range(10), range(1, 11)))
print('s3:', s3)
print('s4:', s4)


print('\n' + '=' * 80) 


"""


# ==========================================================


"""

print('=' * 80 + '\n') 
print('\t\t\tgen.filter.py\n')

cubes = [x**3 for x in range(10)]  
print('cubos:', cubes)              # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print()

print('n     n/2   residuo')
for n in cubes:
    print(n,'   ', n // 2,'   ', n % 2) 
print()

 
odd_cubes1 = filter(lambda cube: cube % 2, cubes)
odd_cubes2 = (cube for cube in cubes if cube % 2)

# Aquí sólo se presentan las direcciones de momoria.
print('odd_cubes1:', odd_cubes1)    # <filter object at 0x000002AFDCF73FA0>
print('odd_cubes2:', odd_cubes2)    # <generator object <genexpr> at 0x000001C5415D8F90>
print()

# Aquí las variables odd_cubes1 y odd_cubes1 se vacían luego de utilizarlas.
# print('odd_cubes1:', list(odd_cubes1))  # [1, 27, 125, 343, 729]
# print('odd_cubes2:', list(odd_cubes2))  # [1, 27, 125, 343, 729]

# odd_cubes1 y odd_cubes2 se vacían luego de la signación.
l_odd_cubes1 = list(odd_cubes1)
l_odd_cubes2 = list(odd_cubes2)

print('l_odd_cubes1:', l_odd_cubes1)
print('l_odd_cubes2:', l_odd_cubes2)
# Las nuevas variables se pueden utilizar cuantas veces se quiera no se vacían. 
# print('l_odd_cubes1:', l_odd_cubes1)   
# print('l_odd_cubes2:', l_odd_cubes2)
print()

# Demostración que odd_cubes1 y odd_cubes2 se vacían luego de la signación.
print('odd_cubes1:', list(odd_cubes1))
print('odd_cubes2:', list(odd_cubes2))
print(); print()



import pprint

d_cubos_1 = dict((c, k) for c, k in enumerate(cubes, 1))
print('d_cubos_1:', d_cubos_1)
pprint.pprint(d_cubos_1)
print()

d_cubos_2 = {k:c for k, c in enumerate(cubes, 1)}
print('d_cubos_2:', d_cubos_2)
pprint.pprint(d_cubos_2)
print(); print()



d_odd_cubes1 = {k:c for k, c in enumerate(l_odd_cubes1, 1)}
print('d_odd_cubes1:', d_odd_cubes1)
pprint.pprint(d_odd_cubes1)
print()

d_odd_cubes2 = dict((k, c) for k, c in enumerate (l_odd_cubes2, 1))
print('d_odd_cubes2:', d_odd_cubes2)
pprint.pprint(d_odd_cubes2)



print('\n' + '=' * 80) 


#==========================================================


print()
print('\t\t\tPráctica\n')

quintuple = [x**5 for x in range(1, 11)]
print('quintuple:', quintuple)
print()

odd_quintuple1 = filter(lambda n: n % 2, quintuple)
l_odd_quintuple1 = list(odd_quintuple1)
print('l_odd_quintuple1:', l_odd_quintuple1)

d_odd_quintuple1 = {k: c for k, c in enumerate(l_odd_quintuple1, 1)}
print('d_odd_quintuple1:', d_odd_quintuple1)

print()


odd_quintuple2 = (n for n in quintuple if n % 2)
l_odd_quintuple2 = list(odd_quintuple2)
print('l_odd_quintuple2:', l_odd_quintuple2)

d_odd_quintuple2 = dict((k, c) for k, c in enumerate(l_odd_quintuple2, 1))
print('d_odd_quintuple2:', d_odd_quintuple2)

print()

import pprint
d_quintuple3 = {k:c for k, c in enumerate(quintuple, 1)}
d_quintuple4 = dict((k, c) for k, c in enumerate(quintuple, 1))
print('d_quintuple:', d_quintuple3)
print('d_quintuple:', d_quintuple4)


print('\n' + '=' * 80) 


"""

# ==========================================================

"""

print('=' * 80 + '\n') 
print('\t\t\tgen.map.filter.py\n')

N = 20 
cubos1 = map(lambda n: (n, n**3), filter(lambda n: n % 3 == 0 or n % 5 == 0, range(N)))
cubos2 = ((n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0)

l_cubos1 = list(cubos1)
l_cubos2 = list(cubos2)

print('l_cubos1:', l_cubos1)
print('l_cubos2:', l_cubos2)


print('\n' + '=' * 80) 


#==========================================================


print()
print('\t\t\tPráctica\n')

cubos3 = ((n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0)
l_cubos3 = list(cubos3)
print('cubos3:', l_cubos3) 
print()



def cubos(n):
    for i in range(n):
        yield i**3 

n = 10
l_c3 = list(cubos(n))
print('l_c3:', l_c3)
print()

cuadrados_cubos3 = ((n, n**2) for n in l_c3 if n % 3 == 0 or n % 5 == 0)
l_cuadrados_cubos3 = list(cuadrados_cubos3)
print('l_cuadrados_c3:', l_cuadrados_cubos3)
print()


print('\n' + '=' * 80) 


"""


# ==========================================================

"""

print('=' * 80 + '\n') 
print('\t\t\tsum.example.py\n')

s1 = sum([n**2 for n in range(10**6)])
s2 = sum((n**2 for n in range(10**6)))
s3 = sum(n**2 for n in range(10**6))
# (10**6) = 1 000 000

print('s1:', s1)
print('s2:', s2)
print('s3:', s3)


print('\n' + '=' * 80) 

"""

# ==========================================================

""" 

print('=' * 80 + '\n') 
print('\t\t\tsum.example.2.py\n')


# s = sum([n**2 for n in range(10**8)])
s2 = sum(n**2 for n in range(10**8))
# print(s)
print(s2)



print('\n' + '=' * 80) 

 """

# ==========================================================

"""

print('=' * 80 + '\n') 
print('\t\t\tperformances.py\n')

from time import time 
# mx = 5500
mx = 5

t = time()    # start time for the for loop
dmloop = []
print('time(): {:.4f} s     '.format(time()), time())
print('t     : {:.4f} s     '.format(t), t)
print()

print('loop:\n')
print('(a, b) divmod(a, b)')
for a in range(1, mx):
    for b in range(a, mx):
        dmloop.append(divmod(a, b))
        print((a, b), '     ', divmod(a, b))
print()
    
print('for loop: {:.4f} s'.format(time() - t))
print('dmloop:', dmloop)    #
print('time() - t: ', time(), '-', t, '=', '{:.4f}'.format(time() - t))  
print()

t = time()  # start time for the list comprehension
dmlist = [divmod(a, b) for a in range(1, mx) for b in range(a, mx)]
print('list comprehension: {:.4f} s'.format(time() - t))
print('dmlist:', dmlist)    #
print()

t = time()  # start time for the generator expression
dmgen = list(divmod(a, b) for a in range(1, mx) for b in range(a, mx))
print('generator expression: {:.4f} s'.format(time() - t))
print('dmgen:', dmgen)      #
print()

print('dmloop = dmlist = dmgen:', dmloop == dmlist == dmgen, '    len(dmloop):', len(dmloop))

 
 
# mx = 10
# for a in range(1, mx):
#     for b in range(a, mx):
#         print(a, b) 


# print(divmod(22, 5)) #(4, 2)


print('\n' + '=' * 80) 

"""

# ==========================================================

"""

print('=' * 80 + '\n') 
print('\t\t\tperformances.map.py\n')

from time import time 

mx = 2 * 10 ** 7
# mx = 2 * 10 ** 2

t = time()
absloop = []
for n in range(mx):
    absloop.append(abs(n))
print('for loop: {:.4f} s'.format(time() - t))
# print('absloop:', absloop)
print()

t = time()
abslist = [abs(n) for n in range(mx)]
print('list comprehension: {:.4f}'.format(time() - t))
# print('abslist:', abslist)
print()

t = time()
absmap = list(map(abs, range(mx)))
print('map: {:.4f}'.format(time() - t))
# print('absmap:', absmap)
print()

t = time()
print(absloop == abslist == absmap, ' :  {:.4f}'.format(time() - t))
print()


print('\n' + '=' * 80) 

# print(list(map(abs, range(10))))


"""


# ==========================================================

"""
print('=' * 80 + '\n') 
print('\t\t\tfunctions.py\n')

def gcd(a, b):      
"""
"""Calcula el Máximo Común Divisor de (a, b). """
"""
    while b != 0:
        print(a, b, a % b, a /b)
        a, b = b, a % b   
        print(a, b)     
    return a

print(gcd(64, 16)); print()
print(gcd(16, 64)); print()
print(gcd(254, 16)); print()
print(gcd(16, 254)); print()


print('\n' + '=' * 80) 


# print(16 / 64, 16 % 64)
# print(64 / 16, 64 % 16)


# mx = 16
# for n in range(1, mx + 1):
#     print(n, '/', mx, '= {:.4f}'.format(n/mx), 'residuo =', n % mx)


"""

# ==========================================================

"""

from functions import gcd
print('=' * 92 + '\n')
print('\t\t\tpythagorean.triple.generation.py\n')

# print(50 ** .5)

N = 50
triples = sorted(((a, b, c) for a, b, c in (
                                            ((m**2 - n**2), (2 * m * n), (m**2 + n**2)) 
                                            for m in range(1, int(N**.5) + 1)
                                            for n in range(1, m)
                                            if (m - n) % 2 and gcd(m, n) == 1
                                            ) if c <= N
                  ), key=lambda * triple: sum(*triple)
                )

print(triples)


print('\n' + '=' * 92)


# ==========================================================

 

print('=' * 94 + '\n') 
print('\t\t\tpythagorean.triple.generation.for.py\n')

from functions import gcd

def gen_triples(N):
    for m in range(1, int(N**.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 and gcd(m, n) == 1:
                c = m**2 + n**2 
                if c <= N:
                    a = m**2 - n**2
                    b = 2 * m * n 
                    yield (a, b, c)
                    
triples = sorted(gen_triples(50), key=lambda *triple: sum(*triple)) 
print(triples)


print('\n' + '=' * 94) 


"""

# ===========================================================
#                     Name localization
# ===========================================================

"""


print('=' * 94 + '\n') 
print('\t\t\tscopes.py\n')

A = 100
ex1 = [A for A in range(5)]
print('for:')
print('A:', A)        # 100
print('ex1:', ex1) 
print()

ex2 = list(A for A in range(5))
print('list:')
print('A:', A)        # 100
print('ex2:', ex2)
print()

ex3 = dict((A, 2 * A) for A in range(5))
print('dict:')
print('A:', A)        # 100
print('ex3:', ex3)
print()

ex4 = set(A for A in range(5))
print('set:')
print('A:', A)        # 100
print('ex4:', ex4)
print()

print()

s = 0 
for A in range(5):
    print('s:', s, '    A:', A)
    s += A 
print('s:', s)

print('A:', A)    # 4


print('\n' + '=' * 94) 


# ==========================================================


print('=' * 94 + '\n') 
print('\t\t\tscopes.noglobal.py\n')

A = 100
ex1 = [A for A in range(5)]
print('A:', A)


print('\n' + '=' * 94) 


# ==========================================================


print('=' * 94 + '\n') 
print('\t\t\tscopes.py\n')

s = 0
for A in range(10):
    s += A
print('s:', s)
print('A:', A) 
print('globals():', globals())


print('\n' + '=' * 94) 


"""



# ===========================================================


"""
print('=' * 94 + '\n') 
print('\t\t\t.py\n')

print('\n' + '=' * 94) 
"""


# ===========================================================

