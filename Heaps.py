class Monticulo:
    def __init__(self, length):
        self.length = length
        self.size = 0
        # Creamos el arreglo de length + 1, dejando el índice 0 de relleno
        self.monticulo = [0] * (length + 1)

    def father(self, i):
        return i // 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def insertArray(self, arr):
        n = len(arr)
        if n > self.length:
            raise ValueError("El arreglo supera la capacidad")
        # Copiamos los elementos empezando desde la posición 1 para que funcionen las fórmulas
        for i in range(n):
            self.monticulo[i + 1] = arr[i]
        
        self.size = n


    def heapify(self, i):
        izq = self.left(i)
        der = self.right(i)
        largest = i
        if izq <= self.size and self.monticulo[izq] > self.monticulo[i]:
            largest = izq

        if der <= self.size and self.monticulo[der] > self.monticulo[largest]:
            largest = der
        if largest != i:
            self.monticulo[i], self.monticulo[largest] = self.monticulo[largest], self.monticulo[i]
            self.heapify(largest)

    def buildHeap(self):
        for i in range(self.father(self.size), 0, -1): #cuenta hasta 1
            self.heapify(i)

 

    def heapSort(self):
        self.buildHeap()
        original_size = self.size
        
        # Recorremos desde el final hasta la segunda posición
        for i in range(original_size, 1, -1):
    
            self.monticulo[1], self.monticulo[i] = self.monticulo[i], self.monticulo[1]
            # Reducir el tamaño lógico del montículo para que heapify no lo incluya
            self.size -= 1
            # Restaurar la propiedad de montículo en la raíz
            self.heapify(1)
            
        # Restauramos el tamaño original del montículo al terminar
        self.size = original_size
        return self.monticulo[1:]
    
    def heapMaximum(self):
        return self.monticulo[1]

    def heapExtractMax(self):
        max = self.heapMaximum()
        self.monticulo[1] = self.monticulo[self.size]
        self.size -= 1
        self.heapify(1)
        return max

    def increaseKey(self, i, key):
        if key < self.monticulo[i]:
            raise ValueError("Debe ser un valor mayor o igual al actual")

        self.monticulo[i] = key
        while i > 1 and self.monticulo[self.father(i)] < self.monticulo[i]:
            self.monticulo[i], self.monticulo[self.father(i)] = self.monticulo[self.father(i)], self.monticulo[i]
            i = self.father(i)

    def maxHeapInsert(self, key):
        self.size += 1
        i =  self.size
        while i > 1 and self.monticulo[self.father(i)] < key:
            self.monticulo[i] = self.monticulo[self.father(i)]
            i = self.father(i)
        self.monticulo[i] = key

if __name__ == '__main__':
    # Instanciamos la clase con capacidad para 10 elementos
    heap = Monticulo(10)

    print("1. Probando insertArray y buildHeap:")
    arr_inicial = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap.insertArray(arr_inicial)
    print(f"Arreglo insertado (sin formato de montículo): {heap.monticulo[1:heap.size+1]}")

    heap.buildHeap()
    print(f"Tras buildHeap (debe cumplir propiedad de Max-Heap): {heap.monticulo[1:heap.size+1]}")
    print("-" * 40)

    print("2. Probando heapExtractMax:")
    maximo = heap.heapExtractMax()
    print(f"Máximo extraído: {maximo}")
    print(f"Montículo tras extracción: {heap.monticulo[1:heap.size+1]}")
    print("-" * 40)

    print("3. Probando increaseKey (incrementar el valor en el índice 9):")
    # Vamos a aumentar el último elemento a un valor muy alto para que suba a la raíz
    heap.increaseKey(9, 15)
    print(f"Montículo tras increaseKey (índice 9 a valor 15): {heap.monticulo[1:heap.size+1]}")
    print("-" * 40)

    print("4. Probando maxHeapInsert:")
    # Extraemos uno más para hacer espacio (capacidad era 10, ahora el size es 9)
    heap.maxHeapInsert(50)
    print(f"Montículo tras insertar 50: {heap.monticulo[1:heap.size+1]}")
    print("-" * 40)

    print("5. Probando heapSort:")
    # heapSort destruirá la estructura del montículo pero devolverá un arreglo ordenado
    arreglo_ordenado = heap.heapSort()
    # Notar que heapSort retorna self.monticulo[1:], por lo que trae los ceros de relleno si el size era menor que la capacidad total.
    # Lo cortamos al tamaño original para verlo limpio:
    print(f"Arreglo ordenado ascendentemente: {arreglo_ordenado[:heap.size]}")