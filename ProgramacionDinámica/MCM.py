import time

def MCM_top_down(i, j, p, dp, s):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    minimo = float('inf')
    for k in range(i, j):
        costo = MCM_top_down(i, k, p, dp, s) + MCM_top_down(k+1, j, p, dp, s) + p[i-1] * p[k] * p[j]
        if costo < minimo:
            minimo = costo
            corte_optimo = k
    dp[i][j] = minimo
    s[i][j] = corte_optimo
    return dp[i][j]

def MCM_bottom_up(p, dp, s):
    n = len(p) - 1
    i = 1
    j = 1
    while i <= n and j <= n:
        dp[i][j] = 0
        i += 1
        j += 1
    
    aux = 2
    while aux < len(p):
        i = 1
        j = aux
        while i <= n and j <= n:
            minimo = float('inf')
            for k in range(i, j):
                costo = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
                if costo < minimo:
                    minimo = costo
                    corte_optimo = k
            dp[i][j] = minimo
            s[i][j] = corte_optimo
            i += 1
            j += 1
        aux += 1
    return dp[1][n]

def reconstruir_parentesis(i, j, s):
    if i == j:
        return f"M_{i}"
    k = s[i][j]
    izq = reconstruir_parentesis(i, k, s)
    der = reconstruir_parentesis(k+1, j, s)
    return f"({izq} x {der})"

if __name__ == '__main__':
    # Datos de entrada
    p = [50, 100, 5, 20, 10]
    n = len(p) - 1

    print("=" * 60)
    print(" MULTIPLICACIÓN DE CADENAS DE MATRICES (MCM) ".center(60))
    print("=" * 60)
    print(f"Vector de dimensiones (p) : {p}")
    print(f"Cantidad de matrices (n)  : {n}\n")

    # ---------------------------------------------------------
    # 1. BENCHMARKING TOP-DOWN (Memorización)
    # ---------------------------------------------------------
    dp_td = [[-1] * (n + 1) for _ in range(n + 1)]
    s_td = [[0] * (n + 1) for _ in range(n + 1)]

    start_td = time.perf_counter()
    costo_td = MCM_top_down(1, n, p, dp_td, s_td)
    end_td = time.perf_counter()

    expresion_td = reconstruir_parentesis(1, n, s_td)
    tiempo_td_ms = (end_td - start_td) * 1000

    print("--- ENFOQUE TOP-DOWN (Recursivo con Memorización) ---")
    print(f"Costo Mínimo      : {costo_td}")
    print(f"Estructura Óptima : {expresion_td}")
    print(f"Tiempo Ejecución  : {tiempo_td_ms:.4f} milisegundos\n")

    # ---------------------------------------------------------
    # 2. BENCHMARKING BOTTOM-UP (Tabulación Iterativa)
    # ---------------------------------------------------------
    dp_bu = [[0] * (n + 1) for _ in range(n + 1)]
    s_bu = [[0] * (n + 1) for _ in range(n + 1)]

    start_bu = time.perf_counter()
    costo_bu = MCM_bottom_up(p, dp_bu, s_bu)
    end_bu = time.perf_counter()

    expresion_bu = reconstruir_parentesis(1, n, s_bu)
    tiempo_bu_ms = (end_bu - start_bu) * 1000

    print("--- ENFOQUE BOTTOM-UP (Iterativo con Tabulación) ---")
    print(f"Costo Mínimo      : {costo_bu}")
    print(f"Estructura Óptima : {expresion_bu}")
    print(f"Tiempo Ejecución  : {tiempo_bu_ms:.4f} milisegundos")
    print("=" * 60)