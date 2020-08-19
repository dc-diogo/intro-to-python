def soma_matrizes(m1, m2):
    lin = len(m1[0])
    col = len(m2)
    lin2 = len(m2[0])
    col2 = len(m2)
    soma = 0
    matriz_somada = []
    linha_somada = []

    
    if lin != lin2 or col != col2:
        return False
    else:
        soma = m1[:]
        for i in range(col):
            linha = m1[i]
            for j in range(lin):
                item_matriz_1 = linha[j]
                item_matriz_2 = m2[i][j]
                soma = item_matriz_1 + item_matriz_2
                linha_somada.append(soma)
            matriz_somada.append(linha_somada)
            linha_somada = []
          
    return matriz_somada    
    

