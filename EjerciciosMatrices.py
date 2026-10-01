import math
 

#Dada una lista invertirla

#opción 1

def invertir1(l): 
    if len(l) == 1:
        return l
    return invertir1(l[1:]) + l[0:1]


l1 = [i for i in range(1,6) ]


print(invertir1(l1))


# opcion 2

def invertir2(l):
    acc = []
    for i in range(len(l)):
        acc.append(l[len(l) - (i + 1)])
    return acc

print(invertir2(l1))

#opción 3

def invertir3(l):
    def combinar(izquierda, derecha):
        acc = derecha + izquierda
        return acc

    def dividir(l):
        if len(l) <= 1:
            return l
        mitad = len(l) // 2
        izquierda = l[:mitad]
        derecha = l[mitad:]
        return combinar(dividir(izquierda), dividir(derecha))
    return dividir(l)


print(invertir3(l1))


#Generar matriz identidad de n dimensiones

def matrizIdentidad(n):
    return  [[ 1 if i == j else 0 for i in range(n)] for j in range (n)]

A = matrizIdentidad(5)
print(A)
    
#Suma de matrices

def sumaMatrices(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    

B = [ [j for j in range(5)] for  i in range(5)]

C = sumaMatrices(A,B)

print(C)


#Matriz transpuesta
def matrizTranspuesta(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


print(matrizTranspuesta(C))

#Multiplicación de matrices 

#Opcion 1

def multiplicacionMatrices1(A, B):
    def productoPunto(u, v):
        acc = 0
        for i in range(len(u)):
            acc += u[i] * v[i]
        return acc


    def multiplicacionAux(A,B):
        if  len(A[0]) == len(B[0]):
            return  [[productoPunto(A[i], B[j]) for j in range(len(B))] for i in range(len(A))]
        return "No está definido"
    
    return multiplicacionAux(A,matrizTranspuesta(B))

print(multiplicacionMatrices1(A, C))
    
#opción 2

def multiplicacionMatrices2(A,B):
    C = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    if len(A[0]) == len(B):
        for i in range(len(A)):
            for j in range(len(B[0])):
                acc = 0
                for k in range(len(B)):
                    acc += A[i][k] * B[k][j]
                C[i][j] = acc
        return C
    

print(multiplicacionMatrices2(A,B))


#Multiplicación matrices por bloques
                
def multiplicacionMatricesPorBloques(A,B):
    def combinar(c11, c12, c21, c22):
        c = [[0 for j in range(2*len(c11))] for i in range(2*len(c11))]
        for i in range(2*len(c11)):
            for j in range(2*len(c11)):
                if i >= 0 and i < len(c11):
                    if j >= 0 and j < len(c11):
                        c[i][j] = c11[i][j]
                    else:
                        c[i][j] = c12[i][j-len(c11)]
                else:
                    if j >= 0 and j < len(c11):
                        c[i][j] = c21[i-len(c11)][j]
                    else:
                        c[i][j] = c22[i-len(c11)][j-len(c11)]
        return c


    def partirMatriz(A):
        mitad = len(A) // 2
        a11  = [[A[i][j] for j in range(mitad)] for i in range(mitad)]
        a12 = [[A[i][j] for j in range(mitad, len(A))] for i in range(mitad)]
        a21 = [[A[i][j] for j in range(mitad)] for i in range(mitad, len(A))]
        a22 = [[A[i][j] for j in range(mitad, len(A))] for i in range(mitad, len(A))]
        return a11, a12, a21, a22

    def organizar(A, n):
        k = math.ceil(math.log(n,2))
        return [[A[i][j] if (i < len(A)) and (j < len(A[0])) else 0 for j in range(2**k)] for i in range(2**k)]
    
    def dividir(A, B):
        
        if  len(A[0]) == 2 and len(A) == len(A[0]) and len(A[0]) == len(B[0]):
            return multiplicacionMatrices1(A,B)
        else:
            a11, a12, a21, a22 = partirMatriz(A)
            b11, b12, b21, b22 = partirMatriz(B)
            c11 = sumaMatrices(dividir(a11, b11), dividir(a12, b21))
            c12 = sumaMatrices(dividir(a11, b12), dividir(a12, b22))
            c21 = sumaMatrices(dividir(a21, b11), dividir(a22, b21))
            c22 = sumaMatrices(dividir(a21, b12), dividir(a22, b22))
            return combinar(c11, c12, c21, c22)
        
    if len(A[0]) == len(B):
        n = max([len(A), len(B), len(A[0]), len(B[0])])
        if n >= 2:
            resultado = dividir(organizar(A,n), organizar(B, n))
            return [[resultado[i][j] for j in range(len(B[0]))] for i in range(len(A))]
        return multiplicacionMatrices1(A,B)
    
    return "No esta definido"

   

        
                    


print(multiplicacionMatricesPorBloques([[1,2,3], [4,5,6], [7,8,9]], matrizIdentidad(3)))



# A es 3x2
D = [
    [1, 2], 
    [3, 4],
    [5, 6]
]

# B es 2x5
E = [
    [1, 0, 2, 1, 3],
    [0, 1, 1, 2, 0]
]

# El resultado esperado (una matriz 3x5) debería ser:
# [[1, 2, 4, 5, 3],
#  [3, 4, 10, 11, 9],
#  [5, 6, 16, 17, 15]]

print(multiplicacionMatricesPorBloques(D, E))

def menorij(A, fila, columna):
    c = [[0 for j in range(len(A[0]) - 1)] for i in range(len(A) - 1)]
    for i in range(len(A) - 1):
        for j in range(len(A[0]) - 1):
            if i < fila:
                if j < columna:
                    c[i][j] = A[i][j]
                else:
                    c[i][j] = A[i][j + 1]
            else:
                if j < columna:
                    c[i][j] = A[i + 1][j]
                else:
                    c[i][j] = A[i + 1][j + 1]
    return c

def determinantesCofactores(A):
    def dividir(A):

        if len(A) == 1:
            return A[0][0]
        
        if len(A) == 2:
            return A[0][0] * A[1][1] - A[0][1] * A[1][0]
        else:
            suma = 0
            for i in range(len(A)):
                suma += A[i][0] * (-1)**i * dividir(menorij(A, i, 0))
            return suma
                
    return dividir(A)




def inversaAPorCofactores(A):
    determinanteA = determinantesCofactores(A)
    if determinanteA  == 0:
        return "no tiene inversa"
    else:  
        return matrizTranspuesta([[(-1)**(i+j) * (1 / determinanteA) * determinantesCofactores(menorij(A, i, j)) for j in range(len(A[0])) ] for i in range(len(A))])
    

def solucionSistemaEcuacionesPorAdjunta(A, b):
    b_columna = [[b[i]] for i in range(len(b))]
    inv = inversaAPorCofactores(A)
    
    if inv == "no tiene inversa":
        return "no tiene solución"
        
    return multiplicacionMatricesPorBloques(inv, b_columna)

# ==========================================
# PRUEBAS INDEPENDIENTES
# ==========================================

# Definimos una matriz A y un vector b (como lista simple)
matriz_A = [
    [2, 1],
    [5, 3]
]
vector_b = [5, 13] 
# Sistema: 
# 2x + y = 5
# 5x + 3y = 13
# Solución esperada: x=2, y=1

# --- 1. Prueba de Determinante ---
print("1. Determinante de A:")
det = determinantesCofactores(matriz_A)
print(f"Resultado: {det}") # Debería ser 1 (2*3 - 5*1)
print("-" * 20)

# --- 2. Prueba de Inversa ---
print("2. Inversa de A:")
inv = inversaAPorCofactores(matriz_A)
for fila in inv:
    print(fila) # Debería ser [[3.0, -1.0], [-5.0, 2.0]]
print("-" * 20)

# --- 3. Prueba de Sistema de Ecuaciones ---
print("3. Solución del Sistema (Ax = b):")
# Gracias a tu cambio, pasamos 'vector_b' directamente como [5, 13]
solucion = solucionSistemaEcuacionesPorAdjunta(matriz_A, vector_b)

if isinstance(solucion, str): # Debería resultar en "no tiene solución"
    print(solucion)
else:
    print(f"Vector x:")
    for fila in solucion:
        print(fila) # Debería resultar en [[2.0], [1.0]]


def matrizAmpliada(A, b):

    acc = [[A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
    for i in range(len(A)):
        # Si b[i] es una lista (para la Inversa), usamos extend()
        # Si b[i] es un número (para Gauss-Jordan), usamos append()
        if isinstance(b[i], list):
            acc[i].extend(b[i])
        else:
            acc[i].append(b[i])
            
    return acc


def FormaEscalonadaReducida(A, n): 
   
    M = [[A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def EscalarFila(k, v):
        M[v] = [k * a for a in M[v]]
    
    def SumarFilas(k, fila_origen, fila_destino):
        M[fila_destino] = [dest + (k * orig) for orig, dest in zip(M[fila_origen], M[fila_destino])]
    
    def cambiarFilas(i, j):
        M[i], M[j] = M[j], M[i]
    
    def limpiarColumna(row, col):
        # Recorremos todas las filas de la matriz
        for i in range(len(M)):
            if i != row:
                # El factor para eliminar el número es su propio valor con signo contrario
                factor = -1 * M[i][col] 
                SumarFilas(factor, row, i)


    def pivoteo():
        fila_pivote = 0
        for j in range(n):
            for i in range(fila_pivote, len(M)):
                if M[i][j] != 0:
                    cambiarFilas(fila_pivote, i)
                    EscalarFila(1 / M[fila_pivote][j], fila_pivote)
                    limpiarColumna(fila_pivote, j)
                    fila_pivote += 1
                    break
                    

        print("Matriz en forma escalonada reducida:")
        print(M)

        return M
        
    # 3. Llamamos a la función principal para que ejecute la transformación
    
    
    # 4. Retornamos la matriz ya reducida
    return pivoteo()

def rango(A):
    M_ampliada = [[A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    rango = 0
    for i in range(len(M_ampliada)):
        fila_nula = True
        for j in range(len(M_ampliada[0])):
            if M_ampliada[i][j] != 0:
                fila_nula = False
                break
        if not fila_nula:
            rango += 1

    return rango


def GauusJordan(A, b):
    n = len(A[0])
    M_ampliada = FormaEscalonadaReducida(matrizAmpliada(A, b), len(A[0]))
    rangoM_ampliada = rango(M_ampliada)
    A_reducida = [[M_ampliada[i][j] for j in range(n)] for i in range(len(M_ampliada))]
    rangoA = rango(A_reducida)
    if rangoA < rangoM_ampliada:
        print("El sistema no tiene solución")
    if rangoA == rangoM_ampliada and rangoA < n:
        print("El sistema tiene infinitas soluciones")
    if rangoA == rangoM_ampliada and rangoA == n:
        print("El sistema tiene solución única")
    return M_ampliada


def inversa(A):
    n = len(A)
    M_ampliada = FormaEscalonadaReducida(matrizAmpliada(A, matrizIdentidad(len(A))), len(A[0]))
    mitad_Izquierda = [[M_ampliada[i][j] for j in range(n)] for i in range(n)]
    rango_A = rango(mitad_Izquierda)
    if rango_A < n:
        print("La matriz no es invertible")
        return None
    matrizInversa = [[M_ampliada[i][j] for j in range(n, 2*n)] for i in range(n)]
    return matrizInversa









# ==========================================
# PRUEBAS DE LOS 3 TIPOS DE SISTEMAS
# ==========================================

print("=== PRUEBAS GAUSS-JORDAN ===")

# 1. Solución Única
A1 = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b1 = [8, -11, -3]
print("\nPrueba 1: Esperamos Solución Única")
resultado1 = GauusJordan(A1, b1)
for f in resultado1: print(f)

# 2. Infinitas Soluciones (La tercera fila es combinación de las otras)
A2 = [[1, -1, 2], [2, 0, 2], [3, -1, 4]]
b2 = [5, 6, 11]
print("\nPrueba 2: Esperamos Infinitas Soluciones")
resultado2 = GauusJordan(A2, b2)
for f in resultado2: print(f)

# 3. Sin Solución (Contradicción en las ecuaciones)
A3 = [[1, 1], [2, 2]]
b3 = [2, 5]
print("\nPrueba 3: Esperamos Sin Solución")
resultado3 = GauusJordan(A3, b3)
for f in resultado3: print(f)

# ==========================================
# PRUEBAS DE INVERSA
# ==========================================

print("\n=== PRUEBAS INVERSA ===")

# 4. Matriz Invertible
A_inv = [[4, 7], 
         [2, 6]]
print("\nPrueba 4: Esperamos Inversa Exitosa")
inv_resultado = inversa(A_inv)
if inv_resultado:
    for f in inv_resultado: print(f)

# 5. Matriz NO Invertible (La fila 2 es proporcional a la fila 1)
A_no_inv = [[1, 2], 
            [2, 4]]
print("\nPrueba 5: Esperamos Que NO sea invertible")
inversa(A_no_inv)
