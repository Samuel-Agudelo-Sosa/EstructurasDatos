#Enunciado: En este ejercicio, se le dará una palabra. Si la palabra contiene las letras "h", "e", "l", "l" y "o" en ese orden (no necesariamente consecutivas), imprima "YES". De lo contrario, imprima "NO".
def chatRoom(palabra):  
    hola = "hello"
    j = 0
    for i in palabra:
        if i == hola[j]:
            j += 1
            if j == 5:
                return "YES"
    return "NO"

print(chatRoom("ahhellllloou"))
print(chatRoom("hlelo"))
print(chatRoom("ahhellllloou"))