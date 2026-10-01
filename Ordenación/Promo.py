import time
import tracemalloc

# 1. Iniciar el rastreo de memoria
tracemalloc.start()

# 2. Iniciar el cronómetro
start_time = time.perf_counter()

# --- INICIO DE TU ALGORITMO ---
s = input().split()
n = int(s[0])
q = int(s[1])

arr = [int(x) for x in input().split()]
arr.sort(reverse=True)

preciosAcumulados = [0] * n
for i in range(n):
    if i == 0:
        preciosAcumulados[i] = arr[i]
    else:
        preciosAcumulados[i] = preciosAcumulados[i - 1] + arr[i]

for i in range(q):
    s = input().split()
    x = int(s[0])
    y = int(s[1])
    if x != y:
        print(preciosAcumulados[x-1] - preciosAcumulados[x-y-1])
    else:
        print(preciosAcumulados[x-1])
# --- FIN DE TU ALGORITMO ---

# 3. Detener el cronómetro
end_time = time.perf_counter()

# 4. Obtener estadísticas de memoria
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

# --- RESULTADOS DE RENDIMIENTO ---
print("\n" + "="*40)
print("📊 REPORT DE RENDIMIENTO")
print("="*40)
# Multiplicamos por 1000 para ver milisegundos o dejamos en segundos
tiempo_total = end_time - start_time
print(f"⏱️ Tiempo de ejecución : {tiempo_total:.6f} segundos")

# Convertimos bytes a Megabytes (1 MB = 10**6 bytes para simplificar o 2**20 para exactitud binaria)
pico_mb = peak_memory / (1024 * 1024)
print(f"💾 Pico de memoria RAM : {pico_mb:.4f} MB")
print("="*40)