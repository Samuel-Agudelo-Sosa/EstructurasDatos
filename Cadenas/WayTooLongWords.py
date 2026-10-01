#Enunciado: En este ejercicio, se le dará una lista de palabras. Para cada palabra, si la longitud de la palabra es menor o igual a 10, imprímala tal cual. 
# De lo contrario, imprímela de la siguiente manera: imprime la primera letra, luego el número de letras entre la primera y la última letra, y luego la última letra. 
palabras = int(input("Ingrese la cantidad de palabras: "))

for i in range(palabras):
    palabra = input("Ingrese la " + str((i+1)) + " palabra: ")
    if len(palabra) <= 10:
        print(palabra)
    else:
        print(palabra[0] + str((len(palabra) - 2)) + palabra[len(palabra)-1])