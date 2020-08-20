class Ordenador:
    def selecao_direta(self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            # Inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            # Poe o menor elemento encontrado no inicio da sublista
            # trocando de lugar os elementos nas posicoes i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

        return lista

    def bolha(self, lista):
        fim = len(lista)

        # range(inicia do fim do vetor, vá até a posição 0, passo de -1 em -1)
        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]


if __name__ == "__main__":
    lista_sd = [4, 2, 7, 2, 6, 2, 9, 55, 1]
    lista_bs = [4, 2, 7, 2, 6, 2, 9, 55, 1]
    o = Ordenador()
    o.selecao_direta(lista_sd)
    print(lista_sd)
    o.bolha(lista_bs)
    print(lista_bs)
