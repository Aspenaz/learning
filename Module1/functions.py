#
#! [Alert: Deprecated method, do not use]  
#? [Query or question: Should this method be exposed in the public API?]  
#// [CommentedOut: Do not use] 
#todo [Refactor: this method so that it conforms to the API. Create some test cases]   
#* [Important: information is highlighted] 


def gcd(a, b):
    """Calcula el Máximo Común Divisor de (a, b). """
    while b != 0:
        # print(a, b, a % b, a /b)
        a, b = b, a % b   
        # print(a, b)     
    return a