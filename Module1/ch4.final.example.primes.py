from math import sqrt, ceil

def get_primes(n):
    primelist = []
    for candidate in range(2, n + 1):
        is_Prime = True
        root = int(ceil(sqrt(candidate)))
        for prime in primelist:
            if prime > root:
                break
            if candidate % prime == 0:
                is_Prime = False 
                break
        if is_Prime:
            primelist.append(candidate)        
    return primelist

print(get_primes(11))

