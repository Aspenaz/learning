def gcd(a, b):
    """Calcula el Máximo Común Divisor de (a, b). """
    while b != 0:
        # print(a, b, a % b, a /b)
        a, b = b, a % b   
        # print(a, b)     
    return a