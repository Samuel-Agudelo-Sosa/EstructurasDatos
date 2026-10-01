#Enunciado: Dada una palabra, se desea convertirla a mayúscula si todas las letras son mayúsculas o si todas las letras son mayúsculas excepto la primera letra.
#  En caso contrario, se desea devolver la palabra sin cambios.
def capsLock(palabra):#código ASCCI
    def invertir(palabra):
        contador = 0
        for letra in palabra:
            if ord(letra) <= 90:
                contador += 1
        if contador == len(palabra) or len(palabra) == 1: #son todas mayúsculas o es una sola letra
            return True
        if contador == len(palabra) - 1 and ord(palabra[0]) >= 97: #son todas mayúsculas excepto la primera letra
            return True
        return False
    def convertir(palabra):
        resultado = ""
        if invertir(palabra):
            for letra in palabra:
                if ord(letra) <= 90:
                    resultado += chr(ord(letra) + 32)
                else:
                    resultado += chr(ord(letra) - 32)
        
        else:
            for letra in palabra:
                resultado += letra
        return resultado
    return convertir(palabra)



print(capsLock("cAPS"))
print(capsLock("Lock"))
print(capsLock("z"))
print(capsLock("Z"))  
print(capsLock("MUNDO"))

def capsLock_pythonic(palabra):
    if len(palabra) == 1 or palabra[1:].isupper():
        return palabra.swapcase()
    return palabra

# --- Pruebas de fuego ---
print(capsLock_pythonic("cAPS"))    # Salida: Caps
print(capsLock_pythonic("HTTP"))    # Salida: http
print(capsLock_pythonic("z"))       # Salida: Z (cumple la regla porque el resto es vacío)
print(capsLock_pythonic("Hello"))   # Salida: Hello (no se toca)
print(capsLock_pythonic("hELLO"))   # Salida: Hello
 
    
