#Hallar a^n

def exponenciacionRecursiva(a,n):
    if n == 0:
        return 1
    return a * exponenciacionRecursiva(a, n - 1)

print(exponenciacionRecursiva(3,2))


def exponenciacionModularRecursvia(a, n, m):
    if n == 0:
        return 1
    return ((a % m) * exponenciacionModularRecursvia(a, n-1, m)) % m

print(exponenciacionModularRecursvia(3,3,2))


def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

print(mcd(15, 30))


def busquedalineal(l, x, acc):
   if len(l) == 0:
       return -1
   elif x == l[0]:
       return acc
   else:
       return busquedalineal(l[1:], x, acc + 1)


print(busquedalineal([1,2,3,4,5,-1,10], -1, 0))

    
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def factorialIterativo(n):
    acc = 1
    for i in range(1, n + 1):
        acc *= i
    return acc

print(factorialIterativo(5))

def fibonacciIterativo(n):
    a = 0
    b = 1
    for i in range(n-1):
        a,b = b, a + b
    return b

print(fibonacci(10))

print(fibonacciIterativo(10))

