def imprime_matriz(matriz):

    lin = len(matriz[0])
    col = len(matriz)
    for i in range(col):
        linha = matriz[i]
        for j in range(lin):
            if linha.index(linha[j]) == len(linha)-1:
                print(linha[j], end="")
            else:
                print(linha[j], end=" ")
        print()
