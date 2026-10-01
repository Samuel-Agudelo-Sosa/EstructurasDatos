import math
import matplotlib.pyplot as plt

def T(n):
    if n <= 1:
        return 1
    return T(n/3) + T(2*n/3) + n

def Omega(c, n):
    return c * n * math.log(n,3)

def O(c, n):
    return c * n * math.log(n,1.5)

lst = [3**x for x in range(11)]

plt.figure(dpi=150, figsize=(10, 6)) #Aumentar la resolución de la gráfica y su tamaño para que se vea mejor
plt.plot(lst, [T(n) for n in lst], label='T(n)', color='black')
plt.plot(lst, [Omega(1, x) for x in lst], label=r'$\Omega(n \log_3 n)$', color='blue')
plt.plot(lst, [O(2, x) for x in lst], label=r'$O(n \log_{1.5} n)$', color='red')
plt.xscale('log', base=3)
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('T(n), Omega(n log n), O(n log n)')
plt.title('Comparación de T(n) con Omega(n log n) y O(n log n)')

plt.legend()
plt.show()