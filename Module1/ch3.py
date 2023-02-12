
#================simple.for.2.py========================
'''
surnames = ['River1', 'River2', 'River3']
for position in range(len(surnames)):
    print(position, surnames[position])
'''    

#================simple.for.3.py========================
'''
surnames = ['River1', 'River2', 'River3']
for surname in surnames:
    print(surname)
'''   

#================simple.for.4.py========================
'''
surnames = ['River1', 'River2', 'River3']
for position, surname in enumerate(surnames):
    print(position, surname)
'''

#================binary.py========================
""" print()
n = 39 
remainders = []
while n > 0:
    remainder = n % 2 
    remainders.append(remainder)
    n //= 2 
    
remainders = remainders[::-1]
print(remainders)
print() """

#================binary.2.py========================
""" print()
n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)

print(remainders)
remainders = remainders[::-1]
print(remainders)
print() """

#================multiple.sequences.while.py========================
""" print()
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
position = 0
while position < len(people):
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1
print()  """


#================for.no.else.py========================
""" print() 
class DriverException(Exception):
    pass 

people = [('James', 27), ('Kirk', 29), ('Lars', 39), ('Robert', 38)]
driver = None 
for person, age in people:
    #print(person, age)
    if age >= 30:
        driver = (person, age)
        break 

print('Driver:', driver) 
  
if driver is None:
    raise DriverException('Driver not found.')

print()  """


#================for.no.else.py========================
""" 
print() 

primes = []
upto = 10
print(range(upto))
print(range(2, upto))
print(range(2, upto + 1))
print()

for n in range(2, upto + 1):
    print('n:', n)
    is_Prime = True 
    for divisor in range(2, n):
        #print('divisor:', divisor)
        remainder = n % divisor
        print('n % divisor:', n, '%', divisor, '=', remainder)
        if remainder == 0:
            is_Prime = False
            break 
    if is_Prime: 
        print(n, 'Is Prime')
        primes.append(n)
    print()
       
print(primes)
    
print()
"""

#================primes.else.py========================
""" 
print() 

primes = []
upto = 10
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break 
    else:
        primes.append(n)

print(primes)

print() 
"""

#================compress.py========================
""" 
print() 

from itertools import compress
data = range(10)
even_selector = [1, 0] * 10 
odd_selector = [0, 1] * 10 

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print('data:', data)
print('even_selector:', even_selector)
print('odd_selector:', odd_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)

print() 

"""
#================compress.py========================
print() 
from itertools import permutations
print(list(permutations('ABC')))


print() 
