def binario_decimal(binario):
    exponente = len(binario) - 1
    acc = 0
    for i in binario:
        acc += int(i) * pow(2, exponente)
        exponente -= 1
    return acc

def decimal_binario(decimal):
    if decimal == 0: return "0"
    cociente = decimal
    acc = ""
    while cociente != 0:
        valor = cociente % 2
        cociente = cociente // 2
        acc = str(valor) + acc
    return acc

def sumabinaria1(a, b):
    return decimal_binario(binario_decimal(a) + binario_decimal(b))


def sumabinaria2(a,b):
    i = len(a) - 1
    j = len(b) - 1
    acc = ""
    lleva = 0
    while i >= 0 or j >= 0 or lleva != 0:
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0
        resultado = bit_a + bit_b + lleva
        
        acc =  str(resultado % 2) + acc
        lleva = resultado // 2

        i -= 1
        j -= 1

    
    return acc

        
        

        


print(sumabinaria1("1010", "1011"))
print(sumabinaria1("11", "1"))

print(sumabinaria2("1010", "1011"))
print(sumabinaria2("11", "1"))