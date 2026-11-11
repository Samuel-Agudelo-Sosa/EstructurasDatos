import time

def Mochila_top_down(b, w, i, c, dp):
    if i == len(b) or c == 0:
        return 0
    if dp[i][c] is not None:
        return dp[i][c]
    
    # Opción 1: No incluir el elemento
    dp[i][c] = Mochila_top_down(b, w, i+1, c, dp)
    
    # Opción 2: Incluir el elemento (si cabe)
    if w[i] <= c:
        dp[i][c] = max(Mochila_top_down(b, w, i+1, c - w[i], dp) + b[i], dp[i][c])   
    
    return dp[i][c]


def Mochila_buttom_up(b, w, C):
    n = len(b)
    dp = [[0] * (C + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        for c in range(1, C+1):
            if w[i-1] <= c:
                dp[i][c] = max(dp[i-1][c] , b[i-1] + dp[i-1][c-w[i-1]])
            else:
                dp[i][c] = dp[i-1][c]
                
    # Retornamos tanto el valor máximo como la matriz para poder hacer backtracking
    return dp[n][C], dp


def obtener_elementos_bottom_up(b, w, C, dp):
    items = []
    i = len(b)
    c = C
    while i > 0 and c > 0:
        if dp[i][c] != dp[i - 1][c]:
            items.append(i - 1)  # Guardamos el índice del elemento
            c -= w[i - 1]
        i -= 1
    items.reverse()
    return items


if __name__ == '__main__':
    # Datos del ejemplo
    b = [30, 40, 50]  # Beneficios/Valores
    w = [2, 3, 4]     # Pesos
    C_max = 5         # Capacidad máxima de la mochila

    print("=== COMPARATIVA DE RENDIMIENTO: PROBLEMA DE LA MOCHILA ===")

    # ----------------------------------------------------
    # 1. EJECUCIÓN TOP-DOWN
    # ----------------------------------------------------
    dp_top_down = [[None] * (C_max + 1) for _ in range(len(b))]
    
    start_top = time.perf_counter()
    resultado_top = Mochila_top_down(b, w, 0, C_max, dp_top_down)
    end_top = time.perf_counter()
    
    tiempo_top = end_top - start_top

    print(f"\n[ Top-Down (Recursivo + Memo) ]")
    print(f"Ganancia máxima obtenida : {resultado_top}")
    print(f"Tiempo de ejecución      : {tiempo_top:.8f} segundos")

    # ----------------------------------------------------
    # 2. EJECUCIÓN BOTTOM-UP
    # ----------------------------------------------------
    start_bottom = time.perf_counter()
    resultado_bottom, matriz_dp_bottom = Mochila_buttom_up(b, w, C_max)
   
    end_bottom = time.perf_counter()
    
    tiempo_bottom = end_bottom - start_bottom
    elementos_elegidos = obtener_elementos_bottom_up(b, w, C_max, matriz_dp_bottom)

    print(f"\n[ Bottom-Up (Iterativo + Tabla) ]")
    print(f"Ganancia máxima obtenida : {resultado_bottom}")
    print(f"Índices de elementos     : {elementos_elegidos}")
    print(f"Tiempo de ejecución      : {tiempo_bottom:.8f} segundos")