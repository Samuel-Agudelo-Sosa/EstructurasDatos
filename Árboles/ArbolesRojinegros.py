class Node:
    # Se añade nil_node como parámetro para eliminar el uso de 'None'
    def __init__(self, value, nil_node):
        self.value = value
        self.black = False  # Nuevos nodos son rojos por defecto
        self.left = nil_node
        self.right = nil_node
        self.parent = nil_node 

    def __str__(self):
        # Condición de parada para el centinela
        if self.value is None:
            return "."
        color = "N" if self.black else "R"
        izq = str(self.left) if self.left.value is not None else "."
        der = str(self.right) if self.right.value is not None else "."
        return f"({self.value}{color} {izq} {der})"

class BRT:
    def __init__(self):
        # 1. Crear el nodo centinela único sin pasarle un nil_node a sí mismo
        # Usamos un truco asignando los valores post-creación para evitar dependencias
        self.NIL = Node(None, None)
        self.NIL.black = True
        
        # 2. El centinela se apunta a sí mismo para mayor seguridad (opcional pero recomendado)
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.parent = self.NIL
        
        # 3. La raíz inicial apunta al centinela
        self.root = self.NIL

    # Método de ayuda para crear nuevos nodos atados al centinela
    def insert_node(self, value):
        new_node = Node(value, self.NIL)
        # Aquí iría tu lógica de inserción estándar de un BST...
        # ...
        return new_node

    def rotacion_derecha(self, node):
        izq = node.left
        
        # 1. El hijo derecho de 'izq' pasa a ser el hijo izquierdo de 'node'
        node.left = izq.right
        
        # LOGICA CORMEN: Solo asignamos el padre si NO es el centinela
        if izq.right != self.NIL:
            izq.right.parent = node
            
        # 2. 'izq' sube a la posición de 'node'
        izq.parent = node.parent
        if node.parent == self.NIL:
            self.root = izq
        elif node == node.parent.left:
            node.parent.left = izq
        else:
            node.parent.right = izq
            
        # 3. 'node' baja y se convierte en el hijo derecho de 'izq'
        izq.right = node
        node.parent = izq

    def rotacion_izquierda(self, node):
        der = node.right
        
        # 1. El hijo izquierdo de 'der' pasa a ser el hijo derecho de 'node'
        node.right = der.left
        
        # LOGICA CORMEN: Solo asignamos el padre si NO es el centinela
        if der.left != self.NIL:
            der.left.parent = node
            
        # 2. 'der' sube a la posición de 'node'
        der.parent = node.parent
        if node.parent == self.NIL:
            self.root = der
        elif node == node.parent.left:
            node.parent.left = der
        else:
            node.parent.right = der
            
        # 3. 'node' baja y se convierte en el hijo izquierdo de 'der'
        der.left = node
        node.parent = der