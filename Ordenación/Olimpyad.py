 

def olympiad():
    scores = [int(x) for x in input().split()] 
    resultado = 0
    #ordenemos descendentemente
    scores.sort(reverse=True)
    i = 0
    puntaje = ""
    while  i < len(scores) and scores[i] != 0 :
        if puntaje != scores[i]:
            resultado += 1
        puntaje = scores[i]
        i += 1
    return resultado

print(olympiad())
    
