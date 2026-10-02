

def darCambio(cantidad, monedas):
    monedas.sort(reverse=True)
    for i in range(len(monedas)):
        while cantidad >= monedas[i] and cantidad>0:
            cantidad -= monedas[i]
            print("Toma ", monedas[i])
            print("Saldo ", cantidad)
    if cantidad > 0:
        print("Ya no hay cambio")