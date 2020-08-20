import ordenador
import random
import time


class ContaTempos:

    def lista_aleatoria(self, n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000)  # int entre 0 e 999

        return lista

    def compara(self, n):
        lista1 = ct.lista_aleatoria(n)
        lista2 = lista1[:]

        o = ordenador.Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolra demorou", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao direta demorou", depois - antes)


if __name__ == "__main__":

    ct = ContaTempos()
    tamanho_vetor = int(input("Quantidade de numeros a comparar: "))
    ct.compara(tamanho_vetor)
