class String:
    @staticmethod
    def is_palindrome(s, case_sensitive=True):
        s = ''.join(c for c in s if c.isalnum() )
        if case_sensitive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c -1]:
                return False 
            return True
    
    @staticmethod
    def set_(sentence):
        return set(sentence.split() )  
        
  
str = 'Is Palindrome 1'
print(String.is_palindrome(str))

str = 'Radar'
print(String.is_palindrome(str))

str = 'Radar Is Radar Is Radar'
print(String.set_(str))
print(String.is_palindrome(str))


print('\\'*80)


class String2: 
    @classmethod
    def is_palindrome(cls, s, case_sensitive=True):
        s = cls._string(s)
        if case_sensitive:
            s = cls._case_sensitive(s)
            # s = s.lower()
        return cls._is_palindrome(s)
    
    @staticmethod
    def _case_sensitive(s):
        return s.lower()
        
    @staticmethod
    def _string(s):
        return ''.join(c for c in s if c.isalnum())
    
    @staticmethod 
    def _is_palindrome(s):
        for c in range(len(s) // 2):
            if s[c] != s[-c -1]:
                return False
        return True
    
print(String2.is_palindrome('A nut for a jar of tuna'))     # True
print(String2.is_palindrome('A nut for a jar of beans'))    # False

print()

n = String2()
s = 'A nut for a jar of tuna'
print(n.is_palindrome(s))               # True
print(n._string(s))                     # Anutforajaroftuna
print(n._case_sensitive(s))             # a nut for a jar of tuna
print(n._string(n._case_sensitive(s)))  # anutforajaroftuna


