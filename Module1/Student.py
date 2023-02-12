class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def get_from_string(cls, name_string: str):
        first_name, last_name = name_string.split()
        if cls.validate_name(first_name) and cls.validate_name(last_name):
            return cls(first_name, last_name)
        else:
            print('Invalid Names')

    @staticmethod
    def validate_name(name):
        return len(name) <= 10


st1 = Student.get_from_string('Name Surname')
print(st1.first_name) # Name
print(st1.last_name)