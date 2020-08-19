def maiusculas(frase):
    letrasMaiusculas = "" 
    for f in frase:
        if ord(f) in range(65, 90):
            letrasMaiusculas += f

    return letrasMaiusculas

