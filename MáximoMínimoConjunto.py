l = [1, 2, 3, 4, 5]

def maximo(l):
    m = l[0]
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
    return m

def minimo(l):
    m = l[0]
    for i in range(len(l)):
        if l[i] < m:
            m = l[i]
    return m

print(maximo(l))
print(minimo(l))