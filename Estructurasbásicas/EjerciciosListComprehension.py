#Dadas dos listas poner en una nueva lista los elementos que no se repiten en ambas listas.
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

#Solución con for 

nueva_lista = []

for elemento in lista1:
    if elemento not in lista2:
        nueva_lista.append(elemento)

for elemento in lista2:
    if elemento not in lista1:
        nueva_lista.append(elemento)


print(nueva_lista)

#Solución con list comprehension

nueva_lista = [elemento for elemento in lista1 if elemento not in lista2] + [elemento for elemento in lista2 if elemento not in lista1] 

print(nueva_lista)


#Calcular producto cartesiano de dos listas

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

nueva_lista = []

#Solución con for

for i in lista1:
    for j in lista2:
        nueva_lista.append((i,j))
print(nueva_lista)

#Solución con list comprehension

nueva_lista = [(i,j) for i in lista1 for j in lista2]

print(nueva_lista)

#Dada dos listas armar una lista de tuplas de los pares que son distintos entre sí

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

#Solución con for

for i in lista1:
    for j in lista2:
        if i != j:
            nueva_lista.append((i,j))

print(nueva_lista)

#Solución con list comprehension

nueva_lista = [(i,j) for i in lista1 for j in lista2 if i != j]
print(nueva_lista)

#Filtrar peliculas que empiezan por T y fueron lanzadas después del año 2000

peliculas = [ ("Gladiator", 2000), ("The Godfather", 1972), ("The Dark Knight", 2008), ("Pulp Fiction", 1994), ("The Shawshank Redemption", 1994),
                ("The Lord of the Rings: The Return of the King", 2003), ("The Matrix", 1999), ("The Silence of the Lambs", 1991), ("The Green Mile", 1999),
                  ("The Prestige", 2006)]

#Solución con for

for pelicula in peliculas:
    if pelicula[0].startswith("T") and pelicula[1] > 2000:
        nueva_lista.append(pelicula)

print(nueva_lista)

#Solución con list comprehension

nueva_lista = [pelicula for pelicula in peliculas if pelicula[0].startswith("T") and pelicula[1] > 2000]

print(nueva_lista)

#escalarun vector

vector = [1, 2, 3, 4, 5]
escalar = 2
resultado = []
#Solución con for

for i in range(len(vector)):
    resultado.append(vector[i] * escalar)
print(resultado)

#Solución con list comprehension
vector = [1, 2, 3, 4, 5]
escalar = 2
resultado = [elemento * escalar for elemento in vector]

print(resultado)

#Aplanar una matriz o lista de listas

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

resultado = []

#Solución con for
for fila in matriz:
    for elemento in fila:
        resultado.append(elemento)

print(resultado)

#Solución con list comprehension
resultado = [num for fila in matriz for num in fila]
print(resultado)

#generar una matriz de 3*4 repleta de 0

#solucion con for
matriz = []
for i in range(3):
    fila = []
    for j in range(4):
        fila.append(0)
    matriz.append(fila)

print(matriz)

#solucion con list comprehension
matriz = [[0 for columna in range(4)] for fila in range(3)]
print(matriz)
