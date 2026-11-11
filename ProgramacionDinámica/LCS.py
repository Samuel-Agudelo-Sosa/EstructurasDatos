import time

def lcs_top_down_costo(i, j, A, B, memo=None):
    if memo is None:
        memo = {}
    if i == len(A) or j == len(B):
        return 0
    if memo.get((i,j)) is not None:
        return memo[(i,j)]

    if A[i] != B[j]:
        resultado = max(lcs_top_down_costo(i+1, j, A, B, memo), lcs_top_down_costo(i, j+1, A, B, memo))
    else:
        resultado = 1 + lcs_top_down_costo(i+1, j+1, A, B, memo)

    memo[(i,j)] = resultado

    return resultado

#Reconstrucción de la cadena aprovechando la función de arriba de costo

def lcs_top_down_cadena_memo(A, B, memo):
    i, j = 0, 0
    solucion = []
    while i < len(A) and j < len(B):
   
        if A[i] == B[j]:
            solucion.append(A[i])
            i += 1
            j += 1
        else:
          
            opt1 = memo.get((i+1, j), 0)
            opt2 = memo.get((i, j+1), 0)
            if opt1 >= opt2:
                i += 1
            else:
                j += 1
    return "".join(solucion)


def lcs_top_down_cadena_scratch(i, j, A, B, memo=None):
    if memo is None:
        memo = {}
    if i == len(A) or j == len(B):
        return ""
    if memo.get((i,j)) is not None:
        return memo[(i,j)]

    if A[i] != B[j]:
        opt1 = lcs_top_down_cadena_scratch(i+1, j, A, B, memo)
        opt2 = lcs_top_down_cadena_scratch(i, j+1, A, B, memo)
        if len(opt1) >= len(opt2):
            resultado = opt1
        else:
            resultado = opt2
    else:
        resultado = A[i] + lcs_top_down_cadena_scratch(i+1, j+1, A, B, memo)

    memo[(i,j)] = resultado

    return resultado

def lcs_bottom_up_costo(A,B):
    m, n = len(A), len(B)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n], dp

def lcs_cadena(A,B, dp):
    i, j = len(A), len(B)
    solucion = []
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            solucion.append(A[i-1])
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    return "".join(reversed(solucion))



if __name__ == '__main__':
    # Usamos cadenas más largas para que la medición de tiempo sea más evidente
    CADENA1 = "AGGTAB" 
    CADENA2 = "GXTXAYB" 

    print(f"[{'LCS BENCHMARKING':^60}]")
    print(f"Len Cadena 1: {len(CADENA1)} | Len Cadena 2: {len(CADENA2)}")
    print("-" * 64)
    print(f"{'Método':<32} | {'Resultado':<12} | {'Tiempo (s)':<12}")
    print("-" * 64)

    # 1. Top-Down Costo
    mi_memo = {}
    t0 = time.perf_counter()
    costo_td = lcs_top_down_costo(0, 0, CADENA1, CADENA2, mi_memo)
    t1 = time.perf_counter()
    print(f"{'Top-Down: Costo (Llena Memo)':<32} | {costo_td:<12} | {t1 - t0:.6f}")

    # 2. Top-Down Reconstrucción (aprovechando memo)
    t0 = time.perf_counter()
    cadena_rec_td = lcs_top_down_cadena_memo(CADENA1, CADENA2, mi_memo)
    t1 = time.perf_counter()
    print(f"{'Top-Down: Rec. (Usa Memo)':<32} | {cadena_rec_td[:9]+'...':<12} | {t1 - t0:.6f}")

    # 3. Top-Down Reconstrucción desde Cero (cadena en memo)
    t0 = time.perf_counter()
    cadena_scratch_td = lcs_top_down_cadena_scratch(0, 0, CADENA1, CADENA2)
    t1 = time.perf_counter()
    print(f"{'Top-Down: Cadena desde Cero':<32} | {cadena_scratch_td[:9]+'...':<12} | {t1 - t0:.6f}")

    # 4. Bottom-Up Costo
    t0 = time.perf_counter()
    costo_bu, dp_table = lcs_bottom_up_costo(CADENA1, CADENA2)
    t1 = time.perf_counter()
    print(f"{'Bottom-Up: Costo (Llena DP)':<32} | {costo_bu:<12} | {t1 - t0:.6f}")

    # 5. Bottom-Up Reconstrucción
    t0 = time.perf_counter()
    cadena_rec_bu = lcs_cadena(CADENA1, CADENA2, dp_table)
    t1 = time.perf_counter()
    print(f"{'Bottom-Up: Rec. (Usa DP)':<32} | {cadena_rec_bu[:9]+'...':<12} | {t1 - t0:.6f}")
    print("-" * 64)