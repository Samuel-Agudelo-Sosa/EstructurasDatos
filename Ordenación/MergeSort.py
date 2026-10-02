

from turtle import right


def mergeSort(l):
    if len(l) > 1:
        mitad = len(l) // 2 
        l1 = l[:mitad]
        l2 = l[mitad:]
        return MezclarIterativamente(mergeSort(l1), mergeSort(l2))
    return l

def MezclarIterativamente(l1, l2):
   i = 0
   j = 0
   l = []
   while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            l.append(l1[i])
            i += 1
        else:
           l.append(l2[j])
           j += 1 
   while i < len(l1):
        l.append(l1[i])
        i += 1
     
   while j < len(l2):
        l.append(l2[j])
        j += 1   
        
   return l
    

def mezclarRecursivamente(l1, l2):
    def mezclarAux(l1, l2, l):
        if len(l1) > 0 and len(l2)>0:
         if l1[0] <= l2[0]:
            l.append(l1[0])
            return mezclarAux(l1[1:], l2, l)
         else:
            l.append(l2[0])
            return mezclarAux(l1,l2[1:],l)
        elif len(l1) == 0:
           return l + l2
        else:
           return l + l1
        
    return mezclarAux(l1, l2, [])


def mergeSort2(l):
    #creemos copia para no afectar el original
    copia = l[:] # así no afectamos el original
    def divide(l, p, r):#usando índices
        if p < r:
            mitad = (p + r) // 2
            divide(l, p, mitad)
            divide(l, mitad + 1, r)
            MezclarIterativamente2(l, p, mitad, r)
        
    def MezclarIterativamente2(l, p, mitad, r):
        i = p
        j = mitad + 1
        l_aux = []
        while i <= mitad and j <= r:
            if l[i] <= l[j]:
                l_aux.append(l[i])
                i += 1
            else:
                l_aux.append(l[j])
                j += 1
        while i <= mitad:
            l_aux.append(l[i])
            i += 1
        while j <= r:
            l_aux.append(l[j])
            j += 1
        for k in range(len(l_aux)):
            l[p + k] = l_aux[k]


    divide(copia, 0, len(copia) - 1)
    return copia


a = [8,2,4,6,9,7,10,1,5,3]
print(mergeSort(a))
print(mergeSort2(a))
