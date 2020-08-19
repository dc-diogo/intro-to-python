def menor_nome(nomes):
    aux = nomes[0].strip().capitalize()
    for i in nomes:
        i = i.strip()
        i = i.capitalize()
        if len(aux) > len(i):
            aux = i
        else:
            if len(aux) == len(i):
                if aux < i:
                    aux = i

    return aux
