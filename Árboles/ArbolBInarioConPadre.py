class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
    def __str__(self):
        izq = str(self.left) if self.left is not None else "."
        der = str(self.right) if self.right is not None else "."
        return (f"({self.value} {izq} {der})")

class BinaryTree:

    def __init__(self):
        self.root = None

    def search(self, valor):
        currentNode = self.root

        while currentNode:
            if currentNode.value == valor:
                return True
            elif valor < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        return False

    def insert(self, valor):
        new_node = Node(valor)

        if self.root is None:
            self.root = new_node
            return True
        
        currentNode = self.root

        while True:
            if currentNode.value == valor:
                return False
            elif valor < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = new_node
                    new_node.parent = currentNode
                    return
                currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = new_node
                    new_node.parent = currentNode
                    return
                currentNode = currentNode.right

    
    def minimo(self, start_node=None): #start_node es para que lo usen mínimo y máximo
        currentNode = start_node if start_node else self.root
        if currentNode is None:
            return False
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode.value
        

    def maximo(self, start_node=None): 
        currentNode = start_node if start_node else self.root
        if currentNode is None:
            return False
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode.value

    def sucesor(self, node):
        if node.right is None:
            current_node = node
            father = node.parent
            while father is not None and current_node == father.right:
                current_node = father
                father = current_node.parent
            return father.value if father else None
        return self.minimo(node.right)

    def predecesor(self, node):
        if node.left is None:
            current_node = node
            father = node.parent
            while father is not None and current_node == father.left:
                current_node = father
                father = current_node.parent
            return father.value if father else None
        return  self.maximo(node.left)

    def in_order(self):
        def in_order_aux(current_Node):
            if current_Node is not None:
                in_order_aux(current_Node.left)
                print(current_Node.value)
                in_order_aux(current_Node.right)
        in_order_aux(self.root)
    

    def delete(self, valor):
        if self.root is None:
            return False
        current_node = self.root
        while current_node:
            if valor < current_node.value:
                current_node = current_node.left
            elif valor > current_node.value:
                current_node = current_node.right
            else:
                if current_node.left is None:
                    if current_node.parent is not None:
                        if current_node == current_node.parent.right:
                            current_node.parent.right = current_node.right
                        else:
                            current_node.parent.left = current_node.right
                    else:
                        self.root = current_node.right
                    if current_node.right is not None:
                        current_node.right.parent = current_node.parent
                    current_node.parent = None
                    return
                elif current_node.right is None:
                    if current_node.parent is not None:
                        if current_node == current_node.parent.right:
                            current_node.parent.right = current_node.left
                        else:
                            current_node.parent.left = current_node.left
                    else:
                        self.root = current_node.left
                    if current_node.left is not None:
                        current_node.left.parent = current_node.parent
                    current_node.parent = None
                    return
                else:
                    sucesor = current_node.right
                    while sucesor.left:
                        sucesor = sucesor.left
                    new_value = sucesor.value
                    self.delete(sucesor.value)
                    current_node.value = new_value
                    return

# --- ENTRY POINT DE PRUEBA ---
if __name__ == '__main__':
    tree = BinaryTree()

    # 1. Insertar valores (Crearemos un árbol con raíz 50)
    #        50
    #      /    \
    #    30      70
    #   /  \    /  \
    # 20   40  60   80
    print("Insertando nodos...")
    for v in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(v)

    print("\nEstructura inicial (Recorrido In-Order):")
    tree.in_order() # Debería imprimir: 20, 30, 40, 50, 60, 70, 80

   # 3. Probamos la estructura con in_order (debería imprimir de menor a mayor)
    print("\nRecorrido In-Order (debe estar ordenado):")
    tree.in_order()

    # 4. Probamos la búsqueda
    print(f"\n¿Existe el 40 en el árbol?: {tree.search(40)}")
    print(f"¿Existe el 99 en el árbol?: {tree.search(99)}")

    # 5. Probamos los extremos
    print(f"\nValor mínimo del árbol: {tree.minimo()}")
    print(f"Valor máximo del árbol: {tree.maximo()}")

    # 6. Probamos el nodo raíz y sus representaciones __str__
    print(f"\nRaíz del árbol: {tree.root}")
    print(f"Hijo izquierdo de la raíz (30): {tree.root.left}")

    # 2. Probar eliminación de nodo hoja (0 hijos)
    print("\n--- Borrando el 20 (0 hijos) ---")
    tree.delete(20)
    tree.in_order() 

    # 3. Probar eliminación de nodo con 1 hijo
    # Primero insertamos un hijo para el 40 para que tenga 1 hijo
    tree.insert(45)
    print("\n--- Borrando el 40 (1 hijo, tiene al 45) ---")
    tree.delete(40)
    tree.in_order() # El 45 debería tomar su lugar

    # 4. Probar eliminación de nodo con 2 hijos (La prueba de fuego)
    print("\n--- Borrando el 50 (La raíz, tiene 2 hijos) ---")
    tree.delete(50)
    tree.in_order() # Debería seguir perfectamente ordenado
    
    print("\nNueva raíz del árbol tras borrar el 50:")
    print(tree.root) # El sucesor del 50 (el 60) debió tomar su lugar