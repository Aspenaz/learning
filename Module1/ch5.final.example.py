# ===========================================================
#                     One last example
# ===========================================================


print('=' * 94 + '\n') 
print('\t\t\tfibonacci.first.py\n')

def fibonacci(N):   # Retorna todos los números fibonacci hasta N
    result = [0]
    next_n = 1 
    while next_n <= N:
        result.append(next_n)
        next_n = sum(result[-2:])
        print(result)
    return result 

print('fibonacci(0):', fibonacci(0))
print()
print('fibonacci(1):', fibonacci(1))
print()
print('fibonacci(50):', fibonacci(50))
print()


l_result = [0, 1, 2, 3, 4, 5]
print(l_result)
print(l_result[-3:])
print(l_result[-2:])
print(l_result[-1:])
print(l_result[:])
print(sum(l_result[-2:]))


print('\n' + '=' * 94) 


# ===========================================================


print('=' * 94 + '\n') 
print('\t\t\tfibonacci.second.py\n')

def fibonacci(N):
    yield 0
    if N == 0:
        return 
    a = 0
    b = 1 
    while b <= N:
        yield b
        a, b = b, a + b

print('fibonacci(0):  ', list(fibonacci(0)))
print()
print('fibonacci(1):  ', list(fibonacci(1)))
print()
print('fibonacci(50): ', list(fibonacci(50)))
print()



# def cyield(M):
#     for n in range(M):
#         yield n    
# d = list(cyield(5))
# print(d)



print('\n' + '=' * 94) 



# ===========================================================



print('=' * 94 + '\n') 
print('\t\t\tfibonacci.elegant.py\n')

def fibonacci(N):
    a, b = 0, 1
    while a <= N:
        yield a 
        a, b = b, a + b

print('fibonacci(0):  ', list(fibonacci(0)))
print()
print('fibonacci(1):  ', list(fibonacci(1)))
print()
print('fibonacci(2):  ', list(fibonacci(2)))
print()
print('fibonacci(50): ', list(fibonacci(50)))
print()


print('\n' + '=' * 94) 


# ===========================================================

