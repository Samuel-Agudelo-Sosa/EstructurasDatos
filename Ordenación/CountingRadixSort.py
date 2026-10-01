def countingSort(l):
    k = max(l)
    A = l[:]
    B = [0 for i in l]
    C = [0 for i in range(0,k + 1)]
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] +=  C[i-1]
    # recorremos del final (len(A)-1 vamos bajando de a 1) al principio (-1) no se incluye llega hasta 0) 
    for i in range(len(A) - 1, -1, -1): 
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return B

def radixSort(l):
    def countingSortForRadix(l, exp):
        salida = [0 for i in l]
        count = [0 for i in range(10)]
        for i in range(len(l)):
            index = (l[i] // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        for i in range(len(l) - 1, -1, -1):
            index = (l[i] // exp) % 10
            salida[count[index] - 1] = l[i]
            count[index] -= 1
        
        return salida

    k = max(l)
    exp = 1
    while k // exp > 0:
        l = countingSortForRadix(l, exp)
        exp *= 10   


    return l

l = [170, 45, 75, 90, 802, 24, 2, 66]
print(countingSort(l))
print(radixSort(l))
