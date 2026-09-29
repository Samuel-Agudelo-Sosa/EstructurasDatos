from collections import deque
import time
import sys
class Node:
 
    #Clase que representa un nodo del Árbol Binario de Búsqueda.   
    def __init__(self, value):
        self.value = value
        self.left = None  # Hijo Izquierdo 
        self.right = None # Hijo Derecho 

class BinaryTree:
    # arbol binario
    def __init__(self):
        self.root = None # raiz vacia al inicio

    def insert(self, value):
        # inserta por niveles BFS
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        queue = deque([self.root])

        while queue:
            current_node = queue.popleft()
            if current_node.left is None:
                current_node.left = new_node
                break
            elif current_node.right is None:
                current_node.right = new_node
                break
            else:
                queue.append(current_node.left)
                queue.append(current_node.right)
        
    def bfs(self):
        if self.root is not None:
            queue = deque([self.root])
            while queue:
                current_node = queue.popleft()
                print(current_node)
                if current_node.left is not None:
                    queue.append(current_node.left)             
                if current_node.right is not None:
                    queue.append(current_node.right)
    

    def dfs_pre_orden(self):
        def recursive_dfs_pre_orden(current_node):
            if current_node is not None:
                print(current_node)
                recursive_dfs_pre_orden(current_node.left)
                recursive_dfs_pre_orden(current_node.right)
        recursive_dfs_pre_orden(self.root)

    def dfs_in_orden(self):
        def recursive_dfs_in_orden(current_node):
            if current_node is not None:
                recursive_dfs_in_orden(current_node.left)
                print(current_node)
                recursive_dfs_in_orden(current_node.right)
        recursive_dfs_in_orden(self.root)

    def dfs_post_orden(self):
        def recursive_dfs_post_orden(current_node):
            if current_node is not None:
                recursive_dfs_post_orden(current_node.left)
                recursive_dfs_post_orden(current_node.right)
                print(current_node)
        recursive_dfs_post_orden(self.root)

    def dfs_pre_orden_iterativo(self):
        if self.root is not None:
            pila = [self.root]
            while pila:
                current_node = pila.pop()
                print(current_node)
                if current_node.right is not None:
                    pila.append(current_node.right)
                if current_node.left is not None:
                    pila.append(current_node.left)

    def dfs_in_orden_iterativo(self):
        if self.root is not None:
            pila = [(self.root, "p")]
        while pila:
            current_node, estado = pila.pop()
            if estado == "p":
                if current_node.right is not None:
                    pila.append((current_node.right, "p"))
                pila.append((current_node, "r"))
                if current_node.left is not None:
                    pila.append((current_node.left, "p"))
            else:
                print(current_node)

    def dfs_post_orden_iterativo(self):
        if self.root is not None:
            pila = [(self.root, "p")]
        while pila:
            current_node, estado = pila.pop()
            if estado == "p":
                pila.append((current_node, "r"))
                if current_node.right is not None:
                    pila.append((current_node.right, "p"))
                if current_node.left is not None:
                    pila.append((current_node.left, "p"))
            else:
                print(current_node)
    
    def nodoMaximo(self):
        def nodoMaximoRecursivo(current_node, acc):
            if current_node is None:
                return acc
            return max(nodoMaximoRecursivo(current_node.left, max(current_node.value, acc)), nodoMaximoRecursivo(current_node.right, max(current_node.value, acc)))

        if self.root is not None:
            return nodoMaximoRecursivo(self.root, self.root)
    
    @staticmethod
    def son_iguales(current_node1, current_node2):
        # 1. Si ambos son None, vamos bien
        if current_node1 is None and current_node2 is None:
            return True
        
        # 2. Tu escudo protector con los 'is None' al frente
        elif current_node1 is None or current_node2 is None or current_node1.value != current_node2.value:
            return False
        
        # 3. Recursión directa llamando al método de la clase
        else:
            return (BinaryTree.son_iguales(current_node1.left, current_node2.left) and 
                    BinaryTree.son_iguales(current_node1.right, current_node2.right))
        
    #otra forma de hacerlo popular
    @staticmethod
    def son_iguales(nodo1, nodo2): # Pasamos directamente los nodos (o la raíz al principio)
        # 1. Si ambos son None, son iguales
        if nodo1 is None and nodo2 is None:
            return True
        
        # 2. Si ambos existen, sus valores deben coincidir Y sus subárboles también
        if nodo1 is not None and nodo2 is not None:
            return (nodo1.value == nodo2.value and 
                    BinaryTree.son_iguales(nodo1.left, nodo2.left) and 
                    BinaryTree.son_iguales(nodo1.right, nodo2.right))
        
        # 3. Si no entró en ninguno de los de arriba, es porque uno era None y el otro no
        return False

    
    def search_node(self, valor):
        def search_node_recursive(current_node, valor):
            if current_node is None:
                return False
            elif current_node.value == valor:
                return True
            else:
                return search_node_recursive(current_node.left, valor) or search_node_recursive(current_node.right, valor)

        return search_node_recursive(self.root, valor)
    

    def altura_nodo(self, node):
        def altura_nodo_recursive(current_node, altura):
            if current_node is None:
                return altura
            else:
                return max(altura_nodo_recursive(current_node.left, altura+1), altura_nodo_recursive(current_node.right, altura+1))
            
        return altura_nodo_recursive(node, -1)

    
    def altura_nodo_optimizado(self, node):
        def altura_nodo_recursive(current_node):
            # Caso base estándar: un nodo None aporta -1 a la altura
            if current_node is None:
                return -1
            
            # Sumamos 1 por el nivel actual más el máximo de los subárboles
            return 1 + max(altura_nodo_recursive(current_node.left), 
                        altura_nodo_recursive(current_node.right))
            
        return altura_nodo_recursive(node)
    
    def es_balanceado(self):
        def es_balanceado_recursive(current_node):
            if current_node is None:
                return True

            return abs(self.altura_nodo_optimizado(current_node.left) - self.altura_nodo_optimizado(current_node.right)) <= 1 and es_balanceado_recursive(current_node.left) and es_balanceado_recursive(current_node.right)

        return es_balanceado_recursive(self.root)
    
    def es_balanceado_optimizado(self):
        def es_balanceado_recursive(current_node):
            if current_node is None:
                return (True, -1)
            left_result = es_balanceado_recursive(current_node.left)
            right_result = es_balanceado_recursive(current_node.right)
            return ((left_result[0] and right_result[0] 
                     and abs(left_result[1] - right_result[1]) <= 1 ),
                       1 + max(left_result[1], right_result[1]))

        return es_balanceado_recursive(self.root)[0]
    
    def es_balanceado_super_optimizado(self):
        def verificar_balance_y_altura(current_node):
            # Caso base: un nodo vacío tiene altura -1 y está balanceado
            if current_node is None:
                return -1
            
            # 1. Calculamos la altura de la izquierda
            alt_izq = verificar_balance_y_altura(current_node.left)
            if alt_izq == -2: 
                return -2 # Si la izquierda ya está desbalanceada, arrastramos el error
                
            # 2. Calculamos la altura de la derecha
            alt_der = verificar_balance_y_altura(current_node.right)
            if alt_der == -2: 
                return -2 # Si la derecha ya está desbalanceada, arrastramos el error
            
            # 3. ¡El escudo! Comprobamos el balance del nodo actual
            if abs(alt_izq - alt_der) > 1:
                return -2 # Rompemos el flujo devolviendo el código de desbalanceado
                
            # 4. Si todo está bien, devolvemos la altura real de este nodo hacia arriba
            return 1 + max(alt_izq, alt_der)

        # Si la función termina y no devolvió -2, significa que todo el árbol es feliz
        return verificar_balance_y_altura(self.root) != -2
    
    def delete(self, node):
        if self.root is not None:
            cola = deque([(self.root, None)])
            encontrado = None
            while cola:
                current_node,padre = cola.popleft()
                if current_node == node:
                    encontrado = current_node
                    
                if current_node.left is not None:
                    cola.append((current_node.left, current_node))
                if current_node.right is not None:
                    cola.append((current_node.right, current_node))
            if encontrado is not None:
                if padre is None:
                    self.root = None
                    return True
                encontrado.value = current_node.value

                if padre.left == current_node:
                    padre.left = None
                elif padre.right == current_node:
                    padre.right = None
                return True
        
        return False

                        


            

                

                    
    # ==========================================
# SCRIPT DE PRUEBA Y MEDICIÓN DE TIEMPOS
# ==========================================
if __name__ == "__main__":
    print("🤖 Creando un árbol PERFECTAMENTE BALANCEADO...")
    
    arbol_estres = BinaryTree()
    sys.setrecursionlimit(15000)
    
    # Insertamos 5,000 elementos usando el insert por niveles (BFS)
    # Esto creará un árbol gordo, lleno y balanceado
    ELEMENTOS = 5000
    for i in range(ELEMENTOS):
        arbol_estres.insert(i)

    print(f"🌲 Árbol balanceado creado con {ELEMENTOS} nodos.")
    print("-" * 60)
    print(f"{'MÉTODO':<35} | {'RESULTADO':<10} | {'TIEMPO (Segundos)':<20}")
    print("-" * 60)

    # 1. Prueba de la versión Ineficiente O(n^2)
    inicio = time.perf_counter()
    res_ineficiente = arbol_estres.es_balanceado()
    fin = time.perf_counter()
    tiempo_ineficiente = fin - inicio
    print(f"{'1. es_balanceado (O(n^2))':<35} | {str(res_ineficiente):<10} | {tiempo_ineficiente:.6f} s")

    # 2. Prueba de la versión Optimizada O(n) con Tuplas
    inicio = time.perf_counter()
    res_optimizado = arbol_estres.es_balanceado_optimizado()
    fin = time.perf_counter()
    tiempo_optimizado = fin - inicio
    print(f"{'2. es_balanceado_optimizado (O(n))':<35} | {str(res_optimizado):<10} | {tiempo_optimizado:.6f} s")

    # 3. Prueba de la versión Súper Optimizada O(n) con Centinela -2
    inicio = time.perf_counter()
    res_super = arbol_estres.es_balanceado_super_optimizado()
    fin = time.perf_counter()
    tiempo_super = fin - inicio
    print(f"{'3. es_balanceado_super_opt (Poda)':<35} | {str(res_super):<10} | {tiempo_super:.6f} s")
    
    print("-" * 60)
    
    # Métricas de aceleración de hardware
    if tiempo_optimizado > 0 and tiempo_super > 0:
        factor_tupla = tiempo_ineficiente / tiempo_optimizado
        factor_poda = tiempo_ineficiente / tiempo_super
        print(f"🚀 ¡Tu versión de tupla fue {factor_tupla:.1f} veces más rápida que la original!")
        print(f"⚡ ¡La versión con Poda Temprana (-2) fue {factor_poda:.1f} veces más rápida que la original!")


            
            
        
    