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


def dimensoes(matriz):
    linha = len(matriz)
    print(str(len(matriz))+"X"+str(len(matriz[0])))


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


def multiplica_matriz(A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_colunas_A == num_linhas_B

    C = []
    for linha in range(num_linhas_A):
        # Começando uma nova linha
        C.append([])
        for coluna in range(num_colunas_B):
            # Adicionando uma coluna na linha
            C[linha].append(0)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]

    return C


def cria_matriz(num_linhas, num_colunas):

    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(
                input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)
        matriz.append(linha)

    for i in range(num_linhas):
        print(matriz[i])


def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    cria_matriz(lin, col)

    def cria_matriz(num_linhas, num_colunas, valor):

    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)

    for i in range(num_linhas):
        print(matriz[i])a


def cria_matriz_personalizada(num_linhas, num_colunas):
    matriz = []  # lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(
                input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

    return matriz


def tarefa(mat):
    dim = len(mat)
    for i in range(dim):
        print(mat[i][dim-1-i], end="  ")


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    print(multiplica_matriz(A, B))
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    tarefa(mat)
