"""
merge_sort.py
Author: Luan Rodrigues, Marcelo Augusto

Conjunto de funções para implementar o algoritmo de ordenação
MergeSort em Python.

Para maiores intruções sobre as funções, veja as docstrings de cada função
separada.
------
Uso:
------
>>> from merge_sort import merge
>>> vetor_desordenado = [5, 1, 2, 10, 4]
>>> vetor_ordenado = merge(x)
>>> print(vetor_ordenado)
[1, 2, 4, 5, 10]
"""


def intercala(inicio, meio, fim, vector):
    """
    Função que intercala dois vetores previamente ordenados e junta ambos
    em um único vetor de forma ordenada.

    Args:
        inicio: Índice do início do vetor a ser ordenado.
        meio: Índice delimitando o meio do vetor onde separa direita e esquerda
            para serem intercalados.
        fim: Índice do fim do vetor a ser ordenado
        vector: Iterável para ser ordenado.
    """
    w = [0 for i in range(fim - inicio)]

    for i in range(inicio, meio):
        # adiciona os dados da esquerda ao vetor aux
        w[i - inicio] = vector[i]

    for j in range(meio, fim):
        # adiciona os dados da direita ao vetor aux
        w[fim - inicio + meio - j - 1] = vector[j]

    i, j = 0, fim - inicio - 1
    # ponteiros para marca posicoes da esquerda e direita
    # i = ponteiro para posicao do lado esquerdo
    # j = ponteiro para posicao do lado direito

    for k in range(inicio, fim):
        # loop em todos os itens para juntar esquerda + direita

        if w[i] <= w[j]:
            # se o atual da esquerda for o menor, então adiciona
            # ao vetor
            vector[k] = w[i]
            i += 1
        else:
            # se o atual da direita for o menor, então adiciona
            # ao vetor
            vector[k] = w[j]
            j -= 1


def merge(vector, inicio=0, fim=None):
    """
    Função principal do merge sort que ordenado um vetor de elementos
    comparáveis entre si.

    Args:
        vector: Iterável para ser ordenado.
        inicio: Índice do início do vetor a ser ordenado.
        fim: Índice do fim do vetor a ser ordenado

    Returns:
        - Iterável com os elementos ordenados.
    """
    if fim is None:
        fim = len(vector)

    if inicio < fim - 1:
        meio = (inicio + fim) // 2  # divide o vetor em duas partes iguais

        merge(vector, inicio, meio)  # ordena recusivamente a metadre da esquerda
        merge(vector, meio, fim)  # ordena recurvivamente a metade da direita
        intercala(inicio, meio, fim, vector)  # junta ambas as partes ordenadas

    return vector

