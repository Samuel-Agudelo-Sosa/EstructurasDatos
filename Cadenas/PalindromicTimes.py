#Enunciado: En este ejercicio, se le dará una hora en el formato HH:MM. La tarea es encontrar la primera hora palindromica posterior a la hora dada.
# Una hora palindromica es una hora que se lee igual de izquierda a derecha que de derecha a izquierda.
#Si la hora ya es palindromica, igual se debe encontrar la siguiente hora palindromica posterior a la hora dada.

def palindromicTime(time): # O(1) ya que el número de horas y minutos es constante, por lo que el tiempo de ejecución no depende del tamaño de la entrada
    def formatoTiempo(t):
        if t >= 0 and t <= 9:
            t = "0" + str(t)
        else:
            t = str(t)
        return t
      
    def sucesor(time):
        hora = int(time[0:2])
        minuto = int(time[3:len(time)])
        if minuto < 59:
            minuto += 1
        else:
            minuto = 0
            if hora < 23:
                hora += 1
            else:
                hora = 0
        return formatoTiempo(hora) + ":" + formatoTiempo(minuto)
    def isPalindromic(time):
        return time[0] == time[4] and time[1] == time[3]
    time = sucesor(time) # Avanzamos el primer minuto
    while not isPalindromic(time):
        time = sucesor(time) # Actualizamos una sola vez
    return time

print(palindromicTime("23:59")) # devuelve "00:00"
print(palindromicTime("12:21")) # devuelve "13:31"