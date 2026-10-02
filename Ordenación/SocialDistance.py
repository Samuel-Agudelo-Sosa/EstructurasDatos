def evaluar(m, espacios):
    if len(espacios) > m:
        return False
    acc = len(espacios) + espacios[0]
    for i in range(len(espacios)-1):
        acc  += espacios[i]
    return acc <= m 

t = int(input())

for i in range(t):
    s = input().split()
    n = int(s[0])
    m = int(s[1])
    espacios = [int(i) for i in input().split()]
    espacios.sort(reverse=True)
    print("YES" if evaluar(m, espacios) else "NO")

    