
l = [10, 5, 1, 2, 1000, -4, 0, 200]

def BubbleSort1(l):
    for j in range(len(l)-1):
        for i in range(len(l)-j-1):
            if (l[i] > l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
    return l

 
            
def BubbleSort2(l):
    
    for j in range(len(l)-1):
        intercambio = False
        for i in range(len(l)-j-1):
            if (l[i] > l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
                intercambio = True
        if not intercambio:   
            break
            
    return l



def selectionSort(l):
    for i in range(len(l)-1):
        indice_minimo = i
        for j in range(i + 1, len(l)):
            if l[j] < l[indice_minimo]:
                indice_minimo = j
        if i != indice_minimo:
            l[i], l[indice_minimo] = l[indice_minimo], l[i]
    return l

print(BubbleSort1(l))
l = [10, 5, 1, 2, 1000, -4, 0, 200]
print(BubbleSort2(l))
l = [10, 5, 1, 2, 1000, -4, 0, 200]
print(selectionSort(l))