import time

def fib_recursivo(n):
    if n <= 1:
        return n
    else:
        return fib_recursivo(n-1) + fib_recursivo(n-2)

def fib_top_down(n, mem=None):
    if mem is None:
        mem = {0:0, 1:1}
    if mem.get(n) is not None:
        return mem[n]
    else:
        mem[n] = fib_top_down(n-1, mem) + fib_top_down(n-2, mem)
        return mem[n]

def fib_bottom_up(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


    

if __name__ == '__main__':
    N = 40  
    
    print(f"--- COMPARATIVA DE RENDIMIENTO PARA FIBONACCI({N}) ---\n")

    # Medición 1: Recursivo Puro
    t_inicio = time.perf_counter()
    res_rec = fib_recursivo(N)
    t_fin = time.perf_counter()
    print(f"1. Recursivo Puro: \tResultado: {res_rec} \tTiempo: {t_fin - t_inicio:.6f} segundos")

    # Medición 2: Top-Down (Diccionario)
    t_inicio = time.perf_counter()
    res_td = fib_top_down(N)
    t_fin = time.perf_counter()
    print(f"2. Top-Down (Memo):\tResultado: {res_td} \tTiempo: {t_fin - t_inicio:.6f} segundos")

    # Medición 3: Bottom-Up (Arreglo)
    t_inicio = time.perf_counter()
    res_bu = fib_bottom_up(N)
    t_fin = time.perf_counter()
    print(f"3. Bottom-Up (Tab):\tResultado: {res_bu} \tTiempo: {t_fin - t_inicio:.6f} segundos")
