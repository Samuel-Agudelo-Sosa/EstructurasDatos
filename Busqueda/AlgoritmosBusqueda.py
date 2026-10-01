l1 = list(range(1,6))

def busquedaLineal(l, x):
    for i in range(len(l)):
        if x == l[i]:
            return i
    return False

print(busquedaLineal(l1, 5))


l2 = list(range(1,101))

def busquedaBinaria(l, x):
    inicio = 0
    fin = len(l) - 1
    while inicio < fin:
        medio = (inicio + fin) // 2
        if l[medio] == x:
            return medio
        elif l[medio] < x:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

print(busquedaBinaria(l2, 50.1))

        

