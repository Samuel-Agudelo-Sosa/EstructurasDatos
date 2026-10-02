l = [35, 12,40, 8, 22, 15]

def insertionSort1(l):
    for i in range(len(l)-1):
        posicion = i
        elemento = l[i+1]
        while posicion >= 0 and l[posicion] > elemento:
            l[posicion + 1] = l[posicion]
            posicion = posicion - 1
        l[posicion + 1] = elemento
    return l


def insertionSort2(l):
    for i in range(1, len(l)):
        elemento = l[i]
        j = i - 1
        while j >= 0 and l[j] > elemento:
            l[ j + 1] = l[j]
            j -= 1
        l[j + 1] = elemento
    return l


def shellSort(l):
    gap = len(l) // 2

    while gap > 0:
        for i in range(gap, len(l)):
            elemento = l[i]
            j = i-gap
            while j >= 0 and l[j] > elemento:
                l[j + gap] = l[j]
                j -= gap
            l[j+gap] = elemento
        gap = gap // 2
    return l

print(insertionSort1(l))
l = [35, 12,40, 8, 22, 15]
print(insertionSort2(l))
l = [35, 12, 40, 8, 22, 15]
print(shellSort(l))