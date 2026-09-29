setA = {"a", "b", "c", "d", "e"}

def conjuntoPotencia(s):
    conjuntoP = [s, set()]
    acc = [{a} for a in s]
    conjuntoP.extend(acc)
    for n in range(1, len(s)-1):
        aux = []
        for a in s:
            for b in acc:
                if a not in b and b.union({a}) not in aux:
                    aux.append(b.union({a}))
        acc = aux
        conjuntoP.extend(acc)
    return conjuntoP
    

conjuntoPotenciaA = conjuntoPotencia(setA)
print(conjuntoPotenciaA)
print(len(conjuntoPotenciaA))
