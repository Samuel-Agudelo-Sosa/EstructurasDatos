import math
def insertionSort(l):
    for i in range(len(l)-1):
        posicion = i
        elemento = l[i+1]
        while posicion >= 0 and l[posicion] > elemento:
            l[posicion + 1] = l[posicion]
            posicion = posicion - 1
        l[posicion + 1] = elemento
    return l

def bucketSort(l): # solo funciona con números entre 0 y 1, pero se puede adaptar a cualquier rango
    aux = [[] for i in l] 
    for i in l:
        posicion =  math.floor(i * len(l))
        aux[posicion].append(i)
    acc = []
    for j in aux:
        acc += insertionSort(j)

    return acc

def bucketSort2(l): #Adaptación de bucket sort para números enteros positivos, funciona con cualquier rango
    k = max(l)
    aux = [[] for i in l] 
    for i in l:
        posicion =  math.floor(i * len(l) / (k + 1))
        aux[posicion].append(i)
    acc = []
    for j in aux:
        acc += insertionSort(j)

    return acc

def bucketSort3(l): #Adaptación de bucket sort para números enteros positivos, funciona con cualquier rango, y con números negativos también
    k = max(l)
    m = min(l)
    aux = [[] for i in l]
    for i in l:
        posicion =  math.floor((i - m) * len(l) / (k - m + 1))
        aux[posicion].append(i)
    acc = []
    for j in aux:
        acc += insertionSort(j)

    return acc  
    
