#
#! [Alert: Deprecated method, do not use]  
#? [Query or question: Should this method be exposed in the public API?]  
#// [CommentedOut: Do not use] 
#todo [Refactor: this method so that it conforms to the API. Create some test cases]   
#* [Important: information is highlighted] 


class Student:
    name = 'unknown' # class attribute
    def __init__(self):
        self.age = 20  # instance attribute

    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name=',cls.name,', age=', cls.age)
        
        
# ===========================================================
        
        
class Student:
    
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age # instance attribute

    @classmethod
    def getobject(cls):
        return cls('Steve', 25)
    
std = Student.getobject()
print(std.name   )
print(std.age)


# ===========================================================


class MyClass:
    
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
   
    
obj = MyClass()
obj.method()
print(obj.method())
print(MyClass.method(obj))
print(obj.classmethod())
print(obj.staticmethod())


# ===========================================================


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
    
p = Pizza(['cheese', 'tomatoes'])
print(p)

