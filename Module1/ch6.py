#
#! [Alert: Deprecated method, do not use]  
#? [Query or question: Should this method be exposed in the public API?]  
#// [CommentedOut: Do not use] 
#todo [Refactor: this method so that it conforms to the API. Create some test cases]   
#* [Important: information is highlighted] 


# ===========================================================
#                       Decorators
# ===========================================================
"""


print('=' * 94 + '\n') 
print('\t\t\tdecorators/time.measure.start.py\n')

from time import sleep, time

def f():
    sleep(.3)
    
def g():
    sleep(.5)
    
t = time()
f()
print('f took:', time() - t)
print()

t = time()
g()
print('g took:', time() - t)
print()


print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\tdecorators/time.measure.dry.py\n')

from time import sleep, time

def f():
    sleep(.3)
    
def g():
    sleep(.5)
    
def measure(func):
    t = time()
    func()
    print(func.__name__, 'took:', time() - t)
    

measure(f)
measure(g)


print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\tdecorators/time.measure.arguments.py\n')

from time import sleep, time

def f(sleep_time=0.1):
    sleep(sleep_time)
    
def measure(func, *args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, 'took:', time() - t)
    
measure(f, sleep_time=0.3)  # **kwargs = sleep_time=0.3
measure(f, 0.2)             #  *args   = 0.2
measure(f)


print('\n' + '=' * 94) 




# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\tdecorators/time.measure.deco1.py\n')

from time import sleep, time

def f(sleep_time=0.1):
    sleep(sleep_time)
    
def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
    return wrapper

m = measure(f)
m(.2)                   #    *args = 0.2
m(sleep_time=0.3)       # **kwargs = sleep_time=0.3
m()                     #     None = by default (sleep_time=0.1)
print(m.__name__)       #  wrapper


print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\tdecorators/time.measure.deco2.py\n')

from time import sleep, time 
from functools import wraps 

def measure(func):
    @wraps(func)    
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
    return wrapper 

@measure 
def f(sleep_time=0.1):
    sleep(sleep_time)
    
    
f(sleep_time=0.3)
f()
print(f.__name__, ':', f.__doc__)


print();  print()


# Este método f vuelve a ser llamado por medio de measure, 
# por eso se imprime dos veces.
m2 = measure(f) #measure() llama a f, pero f en sí llama a measure, por eso hay dos print.
m2(.5)
m2()
print(m.__name__)



print('\n' + '=' * 94) 


print()


def measure7(func):
    @wraps(func)
    def wrapper(*args, **wpargs):
        t = time()
        func(*args, **wpargs)
        print(func.__name__, 'took', time() - t)
    return wrapper 

@measure7 
def f(sleep_time7=.25):
    sleep(sleep_time7)
    
f()
f(.45)



print('\n' + '=' * 94) 


# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\tdecorators/two.decorators.py\n')

from time import sleep, time 
from functools import wraps 

def measureR(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__,'tookR', time() - t, result)
        return result 
    return wrapper 

@measureR 
def f(sleep_time=.25):
    sleep(sleep_time)
    
    
f()
f(.47)
print(f.__name__,':', f.__doc__)
print(print())


mR = measure(f)
mR(.45)
print()



def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        max = 100
        result = func(*args, **kwargs)
        if result > 100:
            print('Result is too big {0}. Max allowed is {1}.'.format(result, max))
        return result 
    return wrapper


@measureR
@max_result 
def cube(n):
    return n ** 3 


print(cube(2), 'R')
print()
print(cube(5), 'R')
print()




print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\tdecorators/decorators.factory.py\n')

from functools import wraps 

def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(func.__name__, args, *kwargs ,'Result is too big {0}. Max allowed is {1}.'.format(result, threshold))
            return result
        return wrapper
    return decorator

@max_result(75)
def cube(n):
    return n ** 3 

@max_result(100)
def square(n):
    return n ** 2

@max_result(1000)
def multiply(a, b):
    return a * b



print(cube(5), 'C')
print()

print(square(11), 'S')
print()

print(multiply(100, 101), 'M')
print()

print('\n' + '=' * 94) 



"""

# ===========================================================
# ===========================================================
#               Object-oriented programming
# ===========================================================
# ===========================================================




# ===========================================================
#                 The simplest Python class
# ===========================================================

print('=' * 94 + '\n') 
print('\t\t\toop/simplest.class.py\n')

class Simplest():
    pass 


print(type(Simplest))   # class 'type'
print(type(Simplest())) # class '__main__.Simplest'
print()

simp = Simplest()
print(type(simp))       # class '__main__.Simplest'
print(type(simp) == Simplest)       # True
print(type(simp) == Simplest())     # False
print()

simp2 = Simplest
print(type(simp2))      # class 'type'
print(type(simp2) == Simplest)       # False
print(type(simp2) == Simplest())     # False
print()


print('\n' + '=' * 94) 



# =============================================================
#                 Class and object namespaces
# =============================================================



print('=' * 94 + '\n') 
print('\t\t\toop/class.namespaces.py\n')

class Person():
    species = 'Human'
    
print(type(Person))    # class 'type'
print(Person)          # class '__main__.Person'
print(Person.species)  # Human
print()

Person.alive = True 
print(Person.alive)     # True
print()

man = Person()
print(type(man))        # class '__main__.Person'
print(man)
print(man.species)      # Human
print(man.alive)        # True
print()

Person.alive = False 
print(man.alive)        # False
print()

man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname)


print('\n' + '=' * 94) 



# =============================================================
#                   Attribute shadowing
# =============================================================



print('=' * 94 + '\n') 
print('\t\t\toop/class.attribute.shadowing.py\n')

class Point():
    x = 10 
    y = 7 
    
p = Point()

print('p.x:', p.x)
print('p.y:', p.y)

print()

p.x = 12 
print('p.x:', p.x)
print('Point.x:', Point.x)

print()

del p.x 
print('p.x:', p.x)

print()

p.z = 3 
print('p.z:', p.z)
# print(Point.z)      # AttributeError: type object 'Point' has no attribute 'z'




print('\n' + '=' * 94) 



# =============================================================
#         I, me, and myself – using the self variable
# =============================================================



print('=' * 94 + '\n') 
print('\t\t\toop/class.self.py\n')

class Square():
    side = 8
    def area(self):
        return self.side ** 2 
    

sq = Square()

print(sq.side, sq.area())       # 8 64
# print(Square.side, Square.area()) # TypeError: area() missing 1 required positional argument: 'self'
print(Square.side, Square.area)   # 8 <function Square.area at 0x000001DCDCF4DE50>
print(Square.side, Square.area(sq)) # 8 64   equivalent to sq.area()

print()

sq.side = 10 
print(sq.side, sq.area())    # 100



print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\toop/class.price.py\n')

class Price():
    def final_price(self, vat, discount=0):
        return (self.net_price * (100 + vat) / 100) - discount
        # return self.net_price ** 2
    

p1 = Price()
p1.net_price = 100 
print(p1.net_price, Price.final_price(p1, 20, 10))
print(p1.net_price, p1.final_price(20, 10))


print('\n' + '=' * 94) 



# =============================================================
#                Initializing an instance
# =============================================================



print('=' * 94 + '\n') 
print('\t\t\toop/class.init.py\n')

class Rectangle():
    def __init__(self, sideA, sideB):
        self.sideA = sideA 
        self.sideB = sideB 
        
    def area(self):
        return self.sideA * self.sideB 
    

r1 = Rectangle(10, 4)
print(r1.sideA, r1.sideB)
print(r1.area())

print()

r2 = Rectangle(7, 3)
print(r2.area())


print()


class Triangle():
    def __init__(self, b, h):
        self.b = b
        self.h = h 
    
    def area(self):
        return (self.b * self.h)/2
    
t1 = Triangle(25, 12)
print('Triangle area:', t1.area())


print('\n' + '=' * 94) 



# =============================================================
#             Inheritance and composition
# =============================================================



print('=' * 94 + '\n') 
print('\t\t\toop/class.inheritance.py\n')

class Engine():
    def start(self):
        print('Engine start')
        pass
    
    def stop(self):
        print('Engine stop')
        pass 
  
    
class ElectricEngine(Engine):  # inherit attributes and methods from the Engine class(base class)
    pass 

class V8Engine(Engine):  # inherit attributes and methods from the Engine class(base class)
    pass 


class Car():
    engine_cls = Engine 
    
    def __init__(self):
        self.engine = self.engine_cls() 
        
    def start(self):
        print('Starting engine {0} for car {1}... '.format(self.engine.__class__.__name__, self.__class__.__name__))
        self.engine.start()
        
    def stop(self):
        print('Stopping engine {0} for car {1}... '.format(self.engine.__class__.__name__, self.__class__.__name__))
        self.engine.stop()


class RaceCar(Car):
    engine_cls = V8Engine 
    
class CityCar(Car):
    engine_cls = ElectricEngine
    
class F1Car(RaceCar):   # F1Car inherits from RaceCar, which inherits from Car. F1Car Is-A RaceCar and RaceCar Is-A Car. F1Car Is-A Car
    engine_cls = V8Engine 
    

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()

cars = [car, racecar, citycar, f1car]

for car in cars:
    car.start()
    car.stop()
    print()
    
    
print('\n' + '=' * 94) 


print('=' * 94 + '\n') 
print('\t\t\toop/class.issubclass.isinstance.py\n')

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()

cars = [(car, 'car'), (racecar, 'racecar'), (citycar, 'citycar'), (f1car, 'f1car')]
car_classes = [Car, RaceCar, CityCar, F1Car]
 

for car, car_name in cars:
    print('Class: {0}     {1}      object: {2}'.format(car.__class__.__name__, car.__class__.engine_cls, car_name) )    
    
print()

for car, car_name in cars:
    for class_ in car_classes:
        belongs = isinstance(car, class_)
        msg = 'is a' if belongs else 'is not a'
        print(car_name, msg, class_.__name__)


print('\n' + '=' * 94 + '\n') 


for class1 in car_classes:
    for class2 in car_classes:
        is_subclass = issubclass(class1, class2)
        msg = '{0} a subclass of'.format('is' if is_subclass else 'is not')
        print(class1.__name__, msg, class2.__name__)

print()





# =============================================================
#                  Accessing a base class
# =============================================================


print('=' * 94 + '\n') 
print('\t\t\toop/super.duplication.py\n')

#  This is quite bad practice because we now
#  have two sets of instructions that are doing the same thing.

class Book:
    def __init__(self, title, publisher, pages):
        self.title = title 
        self.publisher = publisher 
        self.pages = pages 
        
class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        self.title = title 
        self.publisher = publisher 
        self.pages = pages 
        self.format_ = format_ 
        

print('\n' + '=' * 94) 


# ===========================================================


print('=' * 94 + '\n') 
print('\t\t\toop/super.explicit.py\n')

# access a base class from a child

class Book:
    def __init__(self, title, publisher, pages):
        self.title = title 
        self.publisher = publisher 
        self.pages = pages
        
class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        Book.__init__(self, title, publisher, pages)
        self.format_ = format_ 

ebook = Ebook('Learning Python', 'Pack Publishing', 360, 'PDF')
print(ebook.title)
print(ebook.publisher)
print(ebook.pages)
print(ebook.format_)



print('\n' + '=' * 94) 


# ===========================================================


print('=' * 94 + '\n') 
print('\t\t\toop/super.implicit.py\n')

class Book:
    def __init__(self, title, publisher, pages):
        self.title = title 
        self.publisher = publisher 
        self.pages = pages 
        
class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        super().__init__(title, publisher, pages)
        # super(Ebook, self).__init__(title, publisher, pages)
        self.format_ = format_ 
        
ebook = Ebook('Learning Python 2', 'Pack Publishing', 361, 'PDF')
print(ebook.title)
print(ebook.publisher)
print(ebook.pages)
print(ebook.format_)



print('\n' + '=' * 94) 


# =============================================================
#                  Multiple inheritance
# =============================================================



print('=' * 94 + '\n') 
print('\t\t\toop/multiple.inheritance.py\n')

class Shape:
    geometric_type = 'Generic Shape'        # attribute
    
    # def __init__(self, side, type_):
    #     self.side = side
    #     self.geometric_type = type_
    
    def __init__(self, side=1):               # method
        self.side = side
    
    def area(self):                         # method
        raise NotImplementedError
    
    def get_geometric_type(self):           # method
        return self.geometric_type 
    
    def get_side(self):                     # method
        return self.side
    
class Plotter:
    def plot(self, ratio, topleft):
        return ('Plotting at {}, ratio {}.'.format(topleft, ratio))
        
 
                
class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'  
       
class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'
        
        
                
class RegularHexagon(RegularPolygon):
    geometric_type = 'Regular Hexagon'
    
    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)
    
class Square(RegularPolygon):
    geometric_type = 'Square'
    
    def area(self):
        return self.side * self.side 
    
    
# hexagon = RegularHexagon(10, 'Hexagon 3')
hexagon = RegularHexagon(10)
print(hexagon.area())                    # 259.8076211353316
print(hexagon.get_geometric_type())      # Regular Hexagon
hexagon.plot(0.8, (75, 77))              # Plotting at (75, 77), ratio 0.8.
print(hexagon.plot(0.8, (75, 77)))       # Plotting at (75, 77), ratio 0.8.
hexagon.geometric_type = 'Hexagon 2'
print(hexagon.get_geometric_type())
print(hexagon.get_side())
hexagon.side = 11
print(hexagon.get_side())

print()

# square = Square(12, 'Square 3')
square = Square(12)
print(square.get_side())
print(square.area())                     # 144
print(square.get_geometric_type())       # Square
square.plot(0.93, (74, 75))              # Plotting at (74, 75), ratio 0.93.
square.geometric_type = 'Square 2'
print(square.get_geometric_type())
square.side = 14 
print(square.get_side())
print(square.area())

print()

# polygon = Polygon(5, 'Polygon 3')      
polygon = Polygon(5)
print(polygon.get_geometric_type())  
polygon.geometric_type = 'polygon 2'
print(polygon.get_geometric_type())  
print(polygon.get_side())
# print(polygon.area())                 # NotImplementedError

print()

square1 = Square()
square1.geometric_type = 'Square1'
print('area:', square1.area())          # 144
print('side:', square1.get_side())
print('type:', square1.get_geometric_type())
print(square1.plot(0.5, (42, 50)))  

print(square1.__class__.__name__)       # Square

print(square1.__class__.__mro__)        # method resolution order (MRO) is the order in which base classes are searched for a member during lookup.
    # <class '__main__.Square'>, 
    # <class '__main__.RegularPolygon'>, 
    # <class '__main__.Polygon'>, 
    # <class '__main__.Shape'>, 
    # <class '__main__.Plotter'>, 
    # <class 'object'>
print(Square.__mro__)
    # <class '__main__.Square'>, 
    # <class '__main__.RegularPolygon'>, 
    # <class '__main__.Polygon'>, 
    # <class '__main__.Shape'>, 
    # <class '__main__.Plotter'>, 
    # <class 'object'>
print(Square.mro())
    # <class '__main__.Square'>, 
    # <class '__main__.RegularPolygon'>, 
    # <class '__main__.Polygon'>, 
    # <class '__main__.Shape'>, 
    # <class '__main__.Plotter'>, 
    # <class 'object'>
    

print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\toop/mro.simple.py\n')

class A:
    label = 'a'
    
class B(A):
    label = 'b'
    
class C(A):
    label = 'c'
    
class D(B, C):
    pass 

d = D()    
print(d.label)
    
    

print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\toop/mro.py\n')

class A:
    label = 'a'
    
class B(A):
    pass  # was: label = 'b'
    
class C(A):
    label = 'c'
    
class D(B, C):
    pass 

d = D()    
print(d.label)
print(d.__class__.mro())
# <class '__main__.D'>, 
# <class '__main__.B'>, 
# <class '__main__.C'>, 
# <class '__main__.A'>, 
# <class 'object'>


print('\n' + '=' * 94) 



# ===========================================================
# ===========================================================
#                Static and class methods
# ===========================================================
# ===========================================================




# ===========================================================
#                    Static methods
# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\toop/static.methods.py\n')

class String:
        
    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        # Sólo letras y números
        s = ''.join(c for c in s if c.isalnum())
        if case_insensitive:
            print('case_insensitive:', case_insensitive)
            s = s.lower()
            print('s:', s, '\n')
        for c in range(len(s) // 2):
            print(c)
            print('s[c] =', 's[', c, '] =', s[c])
            print('s[-c -1] = s[',-c,'-1] = s[',-c-1,'] =', s[-c -1])
            print()
            if s[c] != s[-c -1]:
                print('s[ c ] != s[-c -1]:')
                print('s[', c, '] != s[',-c, '-1]:')
                print('s[', c, '] != s[',-c-1,']:')
                print('   ', s[c], ' != ', s[-c-1])
                return False 
        return True 

    @staticmethod 
    def get_unique_words(sentence):
        return set(sentence.split())
        # return sentence.split()
        


print('\n1 ', String.is_palindrome('Radar', case_insensitive=False));   print('\\'*80)
print('\n2 ', String.is_palindrome('A nut for a jar of tuna'));     print('\\'*80)
print('\n3 ',String.is_palindrome('Never Odd, Or Even One!'));  print('\\'*80)
print('\n4 ',String.is_palindrome('In Girum Imus Nocte Et Consumimur Igni'));   print('\\'*80)
print('\n5 ',String.get_unique_words('I love palindromes. I really really love them!'));    print('\\'*80)


print('\n' + '=' * 94) 




t = 'A nut for a jar of tuna'
s = ''.join(c for c in t if c.isalnum())
print(s)                 # Anutforajaroftuna
print(s.lower())         # anutforajaroftuna
print(len(s), len(s)//2, len(s)%2)
print(s)

# for c in range(len(s)//2):
#     print(c)

# a = []
# for c in t:
#     if c.isalnum() :
#         a.append(c)
#         print(c)

# print(a)



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\toop/class.methods.factory.py\n')

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        
    @classmethod 
    def from_tuple(cls, coords): 
        return cls(*coords)
    
    @classmethod
    def from_point(cls, point):
        return cls(point.x, point.y)


p = Point.from_tuple((3, 7))
print(p.x, p.y)
print(p)

q = Point.from_point(p)
print(q.x, q.y)

print()

# regular creation    
m = Point(4, 7)
print(m)
print(m.x, m.y)



print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\toop/class.methods.split.py\n')

# If we have no cls in our method, the only option would be to call them 
# like this: String._strip_string(...) and String._is_palindrome(...), 
# which is not good practice. Using cls will act as the class name.

class String:
    
    @classmethod
    def is_palindrome(cls, s, case_insensitive=True):
        s = cls._strip_string(s)        # String._strip_string(s)
        if case_insensitive:
            s = s.lower()
        return cls._is_palindrome(s)    # String._is_palindrome(s)
    
    @staticmethod
    def _strip_string(s):
        return ''.join(c for c in s if c.isalnum())
    
    @staticmethod 
    def _is_palindrome(s):
        for c in range(len(s) // 2): 
            if s[c] != s[-c -1]:
                return False 
        return True 
    
    @staticmethod 
    def get_unique_words(sentence):
        return set(sentence.split())

print(String.is_palindrome('A nut for a jar of tuna'))
print(String.is_palindrome('A nut for a jar of beans'))
print(String.get_unique_words('A nut for a jar of beans, beans, beans'))
print(String._strip_string('A nut for a jar of tuna'))



print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\toop/private.attrs.py\n')

class A:
    def __init__(self, factor):
        self._factor = factor 
        
    def op1(self):
        print('Op1 with factor {}...'.format(self._factor))
        
class B(A):
    def op2(self, factor):
        self._factor = factor 
        print('Op2 with factor {}...'.format(self._factor))     

obj = B(100)
obj.op1()           # Op1 with factor 100...
obj.op2(42)         # Op2 with factor 42...   # when we call obj.op2(42), we modify it, and
obj.op1()           # Op2 with factor 42...   # this reflects in subsequent calls to op1.
                                             


print('\n' + '=' * 94) 



# Si elimino 'self._factor = factor' de Class B 
# entonces el atributo _factor no se modifica.
class A:
    def __init__(self, factor):
        self._factor = factor 
        
    def op1(self):
        print('Op1 with factor {}...'.format(self._factor))
        
class B(A):
    def op2(self, factor):
        # self._factor = factor 
        print('Op2 with factor {}...'.format(self._factor))
        
obj = B(100)
obj.op1()           # Op1 with factor 100...
obj.op2(42)         # Op2 with factor 100...
obj.op1()           # Op1 with factor 100...



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\toop/private.attrs.fixed.py\n')

class A:
    def __init__(self, factor):
        self.__factor = factor 
        
    def op1(self):
        print('Op1 with factor {}...'.format(self.__factor))
        
class B(A):
    def op2(self, factor):
        self.__factor = factor 
        print('Op2 with factor {}...'.format(self.__factor))
        
obj = B(100)
obj.op1()           # Op1 with factor 100...
obj.op2(42)         # Op2 with factor 42...
obj.op1()           # Op1 with factor 100...



print('\n\t\t\toop/private.attrs.py\n')

print(obj.__dict__.keys())      # dict_keys(['_A__factor', '_B__factor'])
print(obj.__dict__)             # {'_A__factor': 100, '_B__factor': 42}
print(obj.__dict__.values())    # dict_values([100, 42])


print('\n' + '=' * 94) 




# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\toop/property.py\n')

class Person:
    def __init__(self, age):
        self.age = age              # anyone can modify this freely
        
class PersonWithAccessors:
    def __init__(self, age):
        self._age = age 
        
    def get_age(self):
        return self._age
    
    def set_age(self):
        if 18 <= age <= 99:
            self._age = age 
        else: 
            raise ValueError('Age must be within [18, 99]')

personwa = PersonWithAccessors(40)
print(personwa.get_age())           # 40
personwa._age = 41                  # modify Ok. data attribute('_age')
print(personwa.get_age())           # 41

personwa.set_age = 42               # can't modify this
print(personwa.get_age())           # 41

PersonWithAccessors._age = 43
print(PersonWithAccessors.get_age)  # <function PersonWithAccessors.get_age at 0x000001ECD3D6C790>
print(personwa.get_age())           # 41

        
# When you decorate a method with property, you can use the name of the method 
# as if it was a 'data attribute'.
class PersonPythonic:
    def __init__(self, age_):
        self._age = age_ 
        
    @property 
    def age(self):
        return self._age 
    
    @age.setter 
    def age(self, age_):
        if 18 <= age_ <= 99:
            self._age = age_ 
        else:
            raise ValueError('Age must be within [18, 99]')
        
# The property decorator also allows for read-only data (no setter) and for 
# special actions when the attribute is deleted.        
person = PersonPythonic(39)
print(person.age)               # 39
person.age = 41                 # name of the method as if it was a data attribute.
print(person.age)               # 41

person._age = 42                # a data attribute.
print(person.age)               # 42
# person.age = 100              #  raise ValueError('Age must be within [18, 99]')
            
    

print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\toop/operator.overloading.py\n')

class Weird:
    def __init__(self, s):
        self._s = s 

    def __len__(self):
        return  len(self._s)
        # return  len(self._s) >= 25             # return boolean value (1 or 0)
        # return  len(self._s) >= 25 in self._s  # 'in <string>' requires string as left operand, not int
    
    def __bool__(self):
        return '42' in self._s
 
msg1 = 'len in str:'
msg2 = '42 in str:'    

weird = Weird('Hello! I am 49 yrs old!')
print('str:', weird._s)
print(msg1, len(weird))
print(msg2, bool(weird))
print()

weird2 = Weird('Hello! I am 42 years old!')
print('str:', weird2._s)
print(msg1, len(weird2))    
print(msg2, bool(weird2))
print()

        
print('\n' + '=' * 94) 



# ===========================================================
# ===========================================================
#             Polymorphism – a brief overview
# ===========================================================
# ===========================================================




# ===========================================================
#                Writing a custom iterator
# ===========================================================


print('=' * 94 + '\n') 
print('\t\t\titerators/iterator.py\n')

class OddEven:   # Odd = Par, Even = Impar
    
    def __init__(self, data):
        self._data = data 
        self.indexes = (list(range(0, len(data), 2)) + list(range(1, len(data), 2)))
           # indexes = [0, 2, 4, 6, 8, 10,  1, 3, 5, 7, 9],   [0, 2,  1, 3]
           
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.indexes: 
            return self._data[self.indexes.pop(0)]
        raise StopIteration 
    
oddeven = OddEven('ThIsIsCoOl!')        # TIICO!hssol
print(''.join(c for c in oddeven)) 
print()

oddeven = OddEven('Halo')
print(''.join(c for c in oddeven))
print()

oddeven = OddEven('Halo')
it = iter(oddeven)
print(next(it))     # 0 H
print(next(it))     # 2 l
print(next(it))     # 1 a
print(next(it))     # 3 o
print()

oddeven = OddEven('Halo')# is not necesary iter
print(next(oddeven))     # 0 H
print(next(oddeven))     # 2 l
print(next(oddeven))     # 1 a
print(next(oddeven))     # 3 o
print()



print('\n' + '=' * 94) 



data = 'ThIsIsCoOl!'
print(range(0, len(data), 2))           # range(0, 11, 2)
print(list(range(0, len(data))))        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Odd:', list(range(0, len(data), 2)))     # [0, 2, 4, 6, 8, 10]   # Odd
print(list(range(1, len(data))))        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Even:', list(range(1, len(data), 2)))     # [1, 3, 5, 7, 9]       # Even
indexes = (list(range(0, len(data), 2)) + list(range(1, len(data), 2)))
print('indexes:', indexes)
print()

data = 'Halo'
print(range(0, len(data), 2))                   # range(0, 4, 2)
print(list(range(0, len(data))))                # [0, 1, 2, 3]
print('Odd:', list(range(0, len(data), 2)))     # [0, 2]         # Odd
print(list(range(1, len(data))))                # [1, 2, 3]
print('Even:', list(range(1, len(data), 2)))    # [1, 3]         # Even
indexes = (list(range(0, len(data), 2)) + list(range(1, len(data), 2)))
print('indexes:', indexes)                      # [0, 2, 1, 3]
print()




data = 'ThIsIsCoOl!'
indexes = list(range(0, len(data), 2)) + list(range(1, len(data), 2))
print('indexes:', indexes)              # [0, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
print('data:', data)
print('     ', indexes)
ip = indexes.pop(0)
print('0', ip, data[ip], indexes)
ip = indexes.pop(1)
print('1', ip, data[ip], indexes)
ip = indexes.pop(2)
print('2', ip, data[ip], indexes)
ip = indexes.pop(3)
print('3', ip, data[ip], indexes)
ip = indexes.pop(4)
print('4', ip, data[ip], indexes)
ip = indexes.pop(5)
print('5', ip, data[ip], indexes)
print()

# TIOhsl 



data = 'ThIsIsCoOl!'
indexes = list(range(0, len(data), 2)) + list(range(1, len(data), 2))
list_odd = list(range(0, len(data), 2))     # [0, 2, 4, 6, 8, 10]
list_even = list(range(1, len(data), 2))    # [1, 3, 5, 7, 9]
print(data, 'len:', len(data))
print('indexes:', indexes, 'len:', len(indexes))
print('list_odd:', list_odd)
print('list_even:', list_even)
print()

print('Odd')
for lo in list_odd:
    print(lo, data[lo], indexes[lo])   # data.pop[lo]: 'str' object has no attribute 'pop'
    # print(lo, data[indexes.pop(lo)])
print()

print('even')
for le in list_even:
    print(le, data[le], indexes[le])
print()




data = 'ThIsIsCoOl!'
indexes = list(range(0, len(data), 2)) + list(range(1, len(data), 2))
print(indexes, len(indexes))
print('0:', indexes.pop(0))
print(indexes, len(indexes))
print('1:', indexes.pop(1))
print(indexes, len(indexes))
print('2:', indexes.pop(2))
print(indexes, len(indexes))
print('3:', indexes.pop(3))
print(indexes, len(indexes))
print('4:', indexes.pop(4))
print(indexes, len(indexes))
print('5:', indexes.pop(5))
print(indexes, len(indexes))
print()




data = 'ThIsIsCoOl!'
indexes = list(range(0, len(data), 2)) + list(range(1, len(data), 2))
for i in indexes:
    print(i)
    print(indexes) # IndexError: pop index out of range
    # print(indexes.pop(i)) 
    # print(indexes)
    print()
    



data = 'ThIsIsCoOl!'
indexes = list(range(0, len(data), 2)) + list(range(1, len(data), 2))
print('{}:\n'.format(data))
list_ipn = []
list_data = []
l = len(indexes)
for n in range(0, l):
    if n <= l:
        print('{}/{}'.format(n, l))
        print(indexes, 'len:', l)
        ipn = indexes.pop(n)
        list_ipn.append(ipn)
        dip = data[ipn]
        list_data.append(dip)
        print(ipn, '"{}"'.format(dip), indexes, 'len:', len(indexes)) # IndexError: pop index out of range
        l = len(indexes)
        print()
    else:
        print('{}/{}'.format(n, l))
        print(indexes, 'len:', l, ' ***{} Out of range {}***'.format(n, l))
        print()
print(list_ipn)
print(list_data)
print(''.join(c for c in list_data))

    
    
    
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

