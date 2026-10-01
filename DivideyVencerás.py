def mergeSort(l):
    def merge(izquierda, derecha): # versión con slice, su ecuación de recurrencia es T(n) = 2T(n/2) + n + n, lo que da O(n log n)
        i = 0
        j = 0
        acc = []
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] <= derecha[j]:
                acc.append(izquierda[i])
                i += 1
            else:
                acc.append(derecha[j])
                j += 1
        while i < len(izquierda):
            acc.append(izquierda[i])
            i += 1
        while j < len(derecha):
            acc.append(derecha[j])
            j += 1
        return acc
    
    def sort(l):
        if len(l) > 1:
            mitad = len(l) // 2
            izquierda = l[:mitad]
            derecha = l[mitad:]
            return merge(sort(izquierda), sort(derecha))
        else:
            return l
    return sort(l)


def maximo(l): #Versión con slice, su ecuación de recurrencia es T(n) = 2T(n/2) + 1 + n, lo que da O(n log n)
    
    def mayor(a, b):
        if a > b:
            return a
        else: 
            return b
    def maximoAux(l):
        if len(l) > 1:
            mitad = len(l) // 2
            izquierda = l[:mitad]
            derecha = l[mitad:]
            return mayor(maximoAux(izquierda), maximoAux(derecha))
        else:
            return l[0]     
    return maximoAux(l)

        

def maximo2(l): #Versión sin Slice, su ecuación de recurrencia es T(n) = 2T(n/2) + 1, lo que da O(n)
    def mayor(a, b):
        if a > b:
            return a
        else:
            return b
        
    def maximoAux(inicio, fin):
        if inicio == fin:
            return l[inicio]
        else:
            mitad = (inicio + fin) // 2
            return mayor(maximoAux(inicio, mitad), maximoAux(mitad + 1, fin))
        
    return maximoAux(0, len(l) - 1)





def BusquedaBinaria(x, l):
    def BusquedaBinariaAux(inicio, fin):
        if inicio > fin:
            return False
        mitad = (inicio + fin) // 2
        if l[mitad] == x:
            return mitad
        elif x < l[mitad]:
            return BusquedaBinariaAux(inicio, mitad - 1)
        else:
            return BusquedaBinariaAux(mitad + 1, fin)


        
    return BusquedaBinariaAux(0, len(l)-1)



def InvertirLista(l):

    def combinar(izquierda, derecha):
        return derecha + izquierda

    def dividir(l):
        if len(l) <= 1:
            return l
        mitad  = len(l) // 2
        izquierda = l[:mitad]
        derecha = l[mitad:]
        return combinar(dividir(izquierda), dividir(derecha))

    return dividir(l)




arr = [2,1,4,6,3,2,12,231,31231,313,13123,13,12]
print(mergeSort(arr))
print(maximo(arr))
print(maximo2(arr))
print(BusquedaBinaria(5, arr))
print(BusquedaBinaria(12, arr))
print(InvertirLista(arr))



def letrasRebeldes(cadena):

    def combinar(izq, der):
        # Si recibimos un estado vacío previo, no lo tratamos como letras
        if izq == "": return der
        if der == "": return izq
        
        i, j = len(izq) - 1, 0
        
        while i >= 0 and j < len(der):
            if izq[i] == der[j]:
                i -= 1
                j += 1
            else:
                break
        
        # El resultado es lo que quedó de la izquierda + lo que sobró de la derecha
        res = izq[:i+1] + der[j:]
        return res
            
    
    def dividir(cadena):
        if len(cadena) <= 1:
            return cadena
        mitad = len(cadena) // 2
        izquierda = dividir(cadena[:mitad])
        derecha = dividir(cadena[mitad:])
        return combinar(izquierda, derecha)
        

    resultado = dividir(cadena)
    return resultado if resultado != "" else "Cadena vacia"



print(letrasRebeldes("aab"))
print(letrasRebeldes("abba"))
print(letrasRebeldes("aaabccddd"))




def torresHanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
          
    else:
        torresHanoi(n-1, origen, auxiliar, destino)
        print(f"Mover disco {n} de {origen} a {destino}")
        torresHanoi(n-1, auxiliar, destino, origen)
        

print("-----------")
torresHanoi(1, "A", "B", "C")
print("-----------")
torresHanoi(2, "A", "B", "C")
print("-----------")
torresHanoi(3, "A", "B", "C")
print("-----------")
torresHanoi(4, "A", "B", "C")

