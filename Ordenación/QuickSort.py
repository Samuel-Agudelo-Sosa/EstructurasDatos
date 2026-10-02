def quickSortHoare(l): # trabaja con dos índices, más eficiente que Lomuto, pero más difícil de entender
        copy = l[:]

        def divide(l, p, r):
            if p < r:
                pivot = partition(l, p, r)
                divide (l, p, pivot-1)
                divide(l,pivot+1, r)

        def partition(l, p, r):
            pivot = l[r]
            i = p
            j = r - 1
            while i <= j:
                while i <= j and l[i] <= pivot:
                    i += 1
                    
                while i <= j and l[j] > pivot:
                    j -= 1
                
                if i < j:
                    l[i], l[j] = l[j], l[i]

            l[r], l[i] = l[i], l[r]
            return i 

        divide(copy, 0, len(copy) - 1)
        return copy


def quickSortLomuto(l): # trabaja con un índice, más fácil de entender pero menos eficiente que Hoare
    copy = l[:]

    def divide(l, p, r):
        if p < r:
            pivot = partition(l, p, r)
            divide (l, p, pivot-1)
            divide(l,pivot+1, r)

    def partition(l, p, r):
        pivot = l[r]
        i = p 
        for j in range(p, r):
            if l[j] <= pivot:
                l[i], l[j] = l[j], l[i]
                i += 1
        l[i], l[r] = l[r], l[i]
        return i

    divide(copy, 0, len(copy) - 1)
    return copy


def quickSortOutPlace(l): # no es in-place, pero es más fácil de entender, y no requiere índices
    
    def dividir(l):
        if len(l) <= 1:
            return l    
        pivote = len(l) - 1
        izquierda = dividir([x for x in l[:-1] if x <= l[pivote]])
        derecha = dividir([x for x in l[:-1] if x > l[pivote]])
        
        return izquierda + [l[pivote]] + derecha

    return dividir(l)

print(quickSortHoare([8,2,4,6,9,7,10,1,5,3]))
print(quickSortLomuto([8,2,4,6,9,7,10,1,5,3]))
print(quickSortOutPlace([8,2,4,6,9,7,10,1,5,3]))