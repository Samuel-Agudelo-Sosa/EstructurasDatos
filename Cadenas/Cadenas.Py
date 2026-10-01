# Tamaño de una cadena
cadena = "hola mundo"
print(len(cadena))

 #subcadena, tiene 3 casos, si no se pone el inicio, se toma como 0, si no se pone el final, se toma como el largo de la cadena, 
 # caso contrario se toman los valores indicados, pero no se incluye el valor del final, es decir, se toma hasta el valor del final - 1
print(cadena[2:4])
print(cadena[:4])
print(cadena[2:])


#reemplaazar una subcadena por otra
# se puede usar el método replace, 
# el primer argumento es la subcadena a reemplazar, el segundo argumento es la subcadena por la que se va a reemplazar, 
# el tercer argumento es opcional y es el número de veces que se va a reemplazar, si no se pone, se reemplaza todas las veces que aparezca la subcadena a reemplazar

print(cadena.replace("hola", "adios"))

# división, se puede usar el método split, el argumento es el separador,
# el separador es opcional si no se pone, se toma como espacio, el resultado es una lista con las subcadenas separadas por el separador
#también recibe un entero opcional que indica el número de veces que se va a dividir, si no se pone, se divide todas las veces que aparezca el separador
print(cadena.split())
print(cadena.split("o"))

#se pueden concatenar cadenas usando el operador +, el resultado es una cadena con las cadenas concatenadas
print("hola" + " " + "mundo")

#concatenación, se puede usar el método join, el argumento es la lista con las subcadenas que se van a concatenar,
# el resultado es una cadena con las subcadenas concatenadas
# el separador es opcional, si no se pone, se toma como espacio, el resultado es una cadena con las subcadenas concatenadas por el separador
print("-".join(["hola", "mundo"]))


#comparación, se compara lexicográficamente, es decir, se compara el valor ASCII de cada carácter, si el primer carácter es igual, se compara el segundo,
#  y así sucesivamente hasta encontrar una diferencia o llegar al final de la cadena, se ordena básicamente por el orden alfabético, 
# pero también se pueden comparar cadenas con caracteres especiales, números, etc.
cadena1 = "hola"
cadena2 = "mundo"
if cadena1 < cadena2:
    print(f"{cadena1} es menor que {cadena2}") # se compara lexicográficamente, el valor ASCII de "h" es menor que el valor ASCII de "m", concuerda con el orden alfabético
elif cadena1 > cadena2:
    print(f"{cadena1} es mayor que {cadena2}")
else:    print(f"{cadena1} es igual a {cadena2}")

#en python las cadenas son vistas como listas de caracteres, por lo que se pueden usar los mismos métodos y operadores que se usan con las listas,
# para recorrerlas podemos hacerlas de dos formas mediante for
for caracter in cadena:
    print(caracter)

for i in range(len(cadena)):
    print(cadena[i])


#operaciones usando código ASCCI con ord y chr, ord devuelve el valor ASCII de un carácter, chr devuelve el carácter correspondiente a un valor ASCII
print(ord("a")) # devuelve 97
print(chr(97)) # devuelve "a"

#ejemplo convertir letra a mayúscula usando código ASCII, se puede usar el método upper, pero también se puede usar el código ASCII para convertir una letra a mayúscula,
# el valor ASCII de "a" es 97, el valor ASCII de "A" es 65, la diferencia es 32, por lo tanto para convertir una letra a mayúscula se le resta 32 al valor ASCII de la letra
#las letras minusculas van de 97 a 122, las letras mayúsculas van de 65 a 90
letra = "a"
letra_mayuscula = chr(ord(letra) - 32)
print(letra_mayuscula) # devuelve "A"

#operaciones usando métodos de las cadenas
print(cadena.upper()) # devuelve la cadena en mayúsculas
print(cadena.lower()) # devuelve la cadena en minúsculas
print(cadena.capitalize()) # devuelve la cadena con la primera letra en mayúscula
print(cadena.title()) # devuelve la cadena con la primera letra de cada palabra en mayúscula