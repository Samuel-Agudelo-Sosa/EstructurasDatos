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


    def insert(self, new_node):
        current_node = self.root
        while True:
            if new_node.value < current_node.value:
                if current_node.left != self.NIL:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    new_node.parent = current_node
                    return True
            elif new_node.value > current_node.value:
                if current_node.right != self.NIL:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    new_node.parent = current_node
                    return True
            else:
                print("No se aceptan repetidos")
                return False

    def fix_insert(self, new_node):
        current_node = new_node
        while current_node != self.root and not current_node.parent.black:
            if current_node.parent == current_node.parent.parent.left:
                uncle = current_node.parent.parent.right
                if not uncle.black:
                    uncle.black = True
                    current_node.parent.black = True
                    current_node.parent.parent.black = False
                    current_node = current_node.parent.parent
                else:
                    if current_node == current_node.parent.right:
                        current_node = current_node.parent
                        self.rotacion_izquierda(current_node)
                
                    current_node.parent.black = True
                    current_node.parent.parent.black = False
                    self.rotacion_derecha(current_node.parent.parent)
            else:
                uncle = current_node.parent.parent.left
                if not uncle.black:
                    uncle.black = True
                    current_node.parent.black = True
                    current_node.parent.parent.black = False
                    current_node = current_node.parent.parent
                else:
                    if current_node == current_node.parent.left:
                        current_node = current_node.parent
                        self.rotacion_derecha(current_node)
                
                    current_node.parent.black = True
                    current_node.parent.parent.black = False
                    self.rotacion_izquierda(current_node.parent.parent)
        self.root.black = True
    

        
    # Método de ayuda para crear nuevos nodos atados al centinela
    def insert_node(self, value):
        new_node = Node(value, self.NIL)
        if self.root == self.NIL:
            self.root = new_node
            new_node.black = True  # La raíz siempre es negra
        else:
            if self.insert(new_node):
                self.fix_insert(new_node)

    

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

    def fix_delete(self, node):
        while node != self.root and node.black:
            if node == node.parent.left:
                brother = node.parent.right
                if not brother.black:
                    brother.black = True
                    node.parent.black = False
                    self.rotacion_izquierda(node.parent)
                    brother = node.parent.right
                if brother.left.black and brother.right.black:
                    brother.black = False
                    node = node.parent
                else:
                    if brother.right.black:
                        brother.left.black = True
                        brother.black = False
                        self.rotacion_derecha(brother)
                        brother = node.parent.right
                    brother.black = node.parent.black
                    node.parent.black = True
                    brother.right.black = True
                    self.rotacion_izquierda(node.parent)
                    node = self.root
            else:
                brother = node.parent.left
                if not brother.black:
                    brother.black = True
                    node.parent.black = False
                    self.rotacion_derecha(node.parent)
                    brother = node.parent.left
                if brother.right.black and brother.left.black:
                    brother.black = False
                    node = node.parent
                else:
                    if brother.left.black:  
                        brother.right.black = True
                        brother.black = False
                        self.rotacion_izquierda(brother)
                        brother = node.parent.left
                    brother.black = node.parent.black
                    node.parent.black = True
                    brother.left.black = True
                    self.rotacion_derecha(node.parent)
                    node = self.root
        node.black = True
        self.NIL.black = True  # Aseguramos que el centinela siempre sea negro
        self.NIL.parent = self.NIL
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL

    def delete(self, valor):
        if self.root is self.NIL:
            return False
            
        current_node = self.root
        
        # 1. Búsqueda del nodo a eliminar
        while current_node != self.NIL:
            if valor < current_node.value:
                current_node = current_node.left
            elif valor > current_node.value:
                current_node = current_node.right
            else:
                # Guardamos el color original del nodo que se va a desconectar
                color_original = current_node.black
                
                # -----------------------------------------------------------
                # CASO 1: El hijo izquierdo es NIL (0 o 1 hijo derecho)
                # -----------------------------------------------------------
                if current_node.left is self.NIL:
                    hijo_reemplazo = current_node.right  # Este nodo toma el lugar de current_node
                    
                    # Reconexión con el padre
                    if current_node.parent is not self.NIL:
                        if current_node == current_node.parent.right:
                            current_node.parent.right = hijo_reemplazo
                        else:
                            current_node.parent.left = hijo_reemplazo
                    else:
                        self.root = hijo_reemplazo
                        
                    # Reconexión del hijo hacia el padre (siempre se ejecuta, incluso si es NIL)
                    hijo_reemplazo.parent = current_node.parent
                    
                    # Si eliminamos un nodo negro, la altura negra se rompe.
                    # Se rebalancea enviando al hijo que subió a tomar su lugar.
                    if color_original:
                        self.fix_delete(hijo_reemplazo)
                    self.NIL.black = True  # Aseguramos que el centinela siempre sea negro
                    self.NIL.parent = self.NIL
                    self.NIL.left = self.NIL
                    self.NIL.right = self.NIL
                    return True

                # -----------------------------------------------------------
                # CASO 2: El hijo derecho es NIL (1 hijo izquierdo)
                # -----------------------------------------------------------
                elif current_node.right is self.NIL:
                    hijo_reemplazo = current_node.left  # Este nodo toma el lugar de current_node
                    
                    # Reconexión con el padre
                    if current_node.parent is not self.NIL:
                        if current_node == current_node.parent.right:
                            current_node.parent.right = hijo_reemplazo
                        else:
                            current_node.parent.left = hijo_reemplazo
                    else:
                        self.root = hijo_reemplazo
                        
                    # Reconexión del hijo hacia el padre
                    hijo_reemplazo.parent = current_node.parent
                    
                    # Rebalanceo de color si el nodo desconectado era negro
                    if color_original:
                        self.fix_delete(hijo_reemplazo)
                    self.NIL.black = True  # Aseguramos que el centinela siempre sea negro
                    self.NIL.parent = self.NIL
                    self.NIL.left = self.NIL
                    self.NIL.right = self.NIL
                    return True

                # -----------------------------------------------------------
                # CASO 3: Tiene 2 hijos
                # -----------------------------------------------------------
                else:
                    # Buscar el sucesor in-order (mínimo del subárbol derecho)
                    sucesor = current_node.right
                    while sucesor.left != self.NIL:
                        sucesor = sucesor.left
                    
                    # Copiamos el valor del sucesor
                    new_value = sucesor.value
                    
                    # La eliminación física ocurre en el sucesor (caerá en Caso 1 o 2
                    # y ejecutará el fix_delete correspondiente si el sucesor era negro)
                    self.delete(sucesor.value)
                    
                    # Asignamos el nuevo valor al nodo actual
                    current_node.value = new_value
                    self.NIL.black = True  # Aseguramos que el centinela siempre sea negro
                    self.NIL.parent = self.NIL
                    self.NIL.left = self.NIL
                    self.NIL.right = self.NIL
                    return True
        self.NIL.black = True  # Aseguramos que el centinela siempre sea negro
        self.NIL.parent = self.NIL
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        return False  # Si el valor no existía en el árbol

    def __str__(self):
        if self.root == self.NIL:
            return "."
        # Invoca automáticamente el __str__ recursivo de la clase Node desde la raíz
        return str(self.root)


# Entry point para probar inserción y eliminación exhaustiva
if __name__ == "__main__":
    arbol = BRT()
    
    # ---------------------------------------------------------
    # 1. FASE DE INSERCIÓN
    # ---------------------------------------------------------
    print("=== FASE DE INSERCIÓN ===")
    valores = [11, 2, 14, 1, 7, 5, 8, 15, 4]
 
    for val in valores:
        arbol.insert_node(val)
        print(f"Insertado {val:2d} -> {arbol}")
        
    print("\nÁrbol resultante final tras todas las inserciones:")
    print(arbol)
    print("-" * 50)


    # ---------------------------------------------------------
    # 2. FASE DE ELIMINACIÓN
    # ---------------------------------------------------------
    print("\n=== FASE DE ELIMINACIÓN ===")
    
    # Prueba A: Borrar un nodo ROJO hoja (No debería disparar rotaciones ni afectar la altura negra)
    # En este árbol, el 4 suele quedar como hoja roja.
    print("\n[Prueba A] Borrando el 4 (Hoja Roja):")
    arbol.delete(4)
    print(arbol)

    # Prueba B: Borrar un nodo NEGRO hoja (Dispara fix_delete y Casos de rebalanceo)
    # El 8 o el 1 suelen quedar como hojas negras.
    print("\n[Prueba B] Borrando el 8 (Hoja Negra - probará el fix_delete):")
    arbol.delete(8)
    print(arbol)
    
    # Prueba C: Borrar un nodo con 1 HIJO
    # Dependiendo de la rotación previa, el 15 o el 14 podrían tener 1 solo hijo
    print("\n[Prueba C] Borrando el 15 (Nodo con 0 o 1 hijo):")
    arbol.delete(15)
    print(arbol)

    # Prueba D: Borrar la RAÍZ (El caso de 2 hijos más extremo)
    # Internamente buscará el sucesor, copiará el valor, y mandará a borrar la hoja
    raiz_actual = arbol.root.value
    print(f"\n[Prueba D] Borrando la raíz actual ({raiz_actual}):")
    arbol.delete(raiz_actual)
    print(f"Nueva raíz: {arbol.root.value}")
    print(arbol)

    # Validar que si busco borrar algo que no existe, no explote
    print("\n[Prueba E] Borrando un número que no existe (99):")
    resultado = arbol.delete(99)
    print(f"Resultado de borrar 99: {resultado}")