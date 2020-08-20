## 1. Matrizes

- **1. Imprimindo matrizes**

  > Escreva uma função **imprime_matriz(matriz)**, que recebe uma matriz como parâmetro e imprime a matriz, linha por linha.  
  > **Arquivo**: imprime_matriz.py

- **2. Tamanho da matriz**

  > Escreva uma função **dimensoes(matriz)** que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.
  > **Arquivo**: dimensoes.py

- **3. Soma de matrizes**

  > Escreva a função **soma_matrizes(m1, m2)** que recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.
  > **Arquivo**: soma.py

- **4: Leitura de matrizes do usuario**

  > O usuário deve inserir a quantidade de linhas e de colunas da matriz e então o programa solicitará os valores para preencher na matriz.
  > **arquivo**: 4. le_matriz.py

- **5: Multiplicação de matrizes**
  > Escreva uma função `multiplica_matriz(A, B)` que recebe 2 parâmetros sendo estes duas matrizes, e retorna a multiplicação desta matriz
  > **arquivo**: 5. multiplicacao_matrizes.py

## 2. Strings

- **1. Valida se é mesma String**

  > Método eh_mesma_string(a, b) recebe duas Strings como parâmetro e informa se é a mesma String ou não
  > **Arquivo:** strings.py

- **2. Devolve primeira string na ordem lixicográfica**
  > Escreva uma função que recebe uma array de Strings como parametro e devolve o primeiro string na ordem lexicografica, ignorando-se letras maiusculas e minusculas
  > **Arquivo:** strings.py

* **3. Letras maiúsculas**

> Escreva a função **maiusculas(frase)** que recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.
> Pode ser útil verificar uma tabela **ASCII**, que contém os valores de cada caractere. Ver https://pt.wikipedia.org/wiki/ASCII
> Para simplificar a solução do exercício, as frases passadas para a sua função não possuirão caracteres que não estejam presentes na tabela ASCII apresentada, como **ç, á, É, ã**, etc.
> **Arquivo:** letras_maiusculas.py

- **4. Menor nome**
  > Escreva uma função **menor_nome(nomes)** que recebe uma lista de strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista.
  > A função deve **ignorar espaços antes e depois do nome** e deve devolver o menor nome presente na lista. Este nome deve ser devolvido com a **primeira letra maiúscula e seus demais caracteres minúsculos**, independente de como tenha sido apresentado na lista passada para a função.
  > Quando houver mais de um nome com o menor comprimento dentre os nomes na lista, a função deve devolver o primeiro nome com o menor comprimento presente na lista.
  >
  > ````
  > menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
  > menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ')
  > menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
  > Resposta: Deve devolver 'José' ```
  > ````

### Strings, funções com números reais e exercícios

- [Strings e arquivos](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula13.html):
- [Mais funções com números reais](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula14.html)
- [Mais funções com reais](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula15.html)
- [Exercícios](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula16.html)

## 3. Classes

- **1. Uma classe para triângulos**
  > Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos lados a, b e c de um triângulo. A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo. Um objeto desta classe deve responder às seguintes chamadas:

```
t.a
# deve devolver o valor do lado a do triângulo
t. b
# deve devolver o valor do lado b do triângulo
t.c
# deve devolver o valor do lado c do triângulo

t.perimetro()
# deve devolver um inteiro correspondente ao valor do perímetro do triângulo.
```

    > Escreva o metodo tipo_lado() que devolve uma string dizendo se o triângulo é: isósceles (dois lados iguais), equilátero (todos os lados iguais), escaleno (todos os lados diferentes).
    > **Arquivo**: triangulos.py

## 4. Ordenação

- **1. Ordenação Seletiva**

  > Escrever um algorítimo de ordenação seletiva
  > **Arquivo**: ordenador.py

- **2. Bubble sort**
  > Escrever um algorítimo de ordenação bubble sort
  > **Arquivo**: ordenador.py
