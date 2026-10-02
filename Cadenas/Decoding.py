#Enunciado: En este ejercicio, se le dará una palabra. Deberá decodificarla utilizando el siguiente método:
#tome la letra del medio de la palabra y colóquela al principio, luego tome la letra del medio de las letras restantes y colóquela después de la letra anterior, y así sucesivamente hasta que no queden letras.
#si es un número par de letras, tome la letra del medio izquierda.
import math
def  decodificar(palabra): #algoritmo recursivo, T(n) = T(n-1) + O(n)  = O(n^2)
    mitad = math.floor((len(palabra) - 1) / 2)
    if len(palabra) == 1:
        return palabra
    return palabra[mitad] + decodificar(palabra[0:mitad] + palabra[mitad+1:len(palabra)])

print(decodificar("volga"))
print(decodificar("abba"))


def decodificar2(palabra):
    res = [] # Usamos lista para evitar el O(n^2) de los strings
    n = len(palabra)
    
    # Vamos de afuera hacia adentro
    for i in range(math.ceil(n / 2)):
        izq = i
        der = n - 1 - i
        
        if izq != der:
            # Insertamos en el orden que tu lógica pide
            # (Si quieres el mismo resultado exacto que la recursiva)
            res.append(palabra[der])
            res.append(palabra[izq])
        else:
            res.append(palabra[der])
            

    return "".join(res[::-1])

print(decodificar2("volga"))
print(decodificar2("abba"))