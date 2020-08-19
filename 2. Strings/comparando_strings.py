
#------------------------------------------------------------#

# Valida se é a mesma String

def eh_mesma_string(a, b):
    if a is b:
        return True
    else:
        return False

#------------------------------------------------------------#

# Escreva uma função que recebe uma rray de Strings como
# parametro e devolve o primeiro string na ordem lexicografica,
# ignorand-se letras maiusculas e minusculas

def menor_string(lista):
    i = 0
    aux = lista[0].lower().strip()
    while i < len(lista):
        lista[i] = lista[i].lower()
        lista[i] = lista[i].strip()
        if aux > lista[i]:
            aux = lista[i]
        i = i + 1

    return aux


lista = [ "Maçã", "  banana  ", "Pera", "uva", "Uva  "]
print(menor_string(lista))

# Implementar o teste

# def testa_menor_string():
#    teste_pontual(["ana", "maria", "José", "Valdemar"])
#------------------------------------------------------------#
