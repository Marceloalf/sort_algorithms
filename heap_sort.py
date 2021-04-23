"""
heap_sort.py
Author: Luan Rodrigues, Marcelo Augusto

Conjunto de funções para implementar o algoritmo de ordenação
HeapSort em Python.

Para maiores intruções sobre as funções, veja as docstrings de cada função
separada.
------
Uso:
------
>>> from heap_sort import heap
>>> vetor_desordenado = [5, 1, 2, 10, 4]
>>> vetor_ordenado = heap(x)
>>> print(vetor_ordenado)
[1, 2, 4, 5, 10]
"""


def max_heapfy(vetor, pai, tamanho):
    """
    Organiza o vetor como uma arvore onde a raiz é
    maior do que ambos os filhos a esquerda e a direita

    Args:
        vetor: Iterável para ser ordenado.
        pai: Índice da raiz da árvore.
        tamanho: Tamanho do vetor para ser aplicado a propriedade.
    """
    filho_esquerda = pai * 2 + 1
    # calculo para indice do filho à esquerda

    filho_direita = pai * 2 + 2
    # calculo para indice do filho à direita

    if filho_esquerda <= tamanho and vetor[filho_esquerda] > vetor[pai]:
        # se o filho à erquerda maior do que a atual raiz, devem ser invertidos
        vetor[pai], vetor[filho_esquerda] = vetor[filho_esquerda], vetor[pai]
        # recursivamente ordena a subarvore à esquerda
        max_heapfy(vetor, filho_esquerda, tamanho)

    if filho_direita <= tamanho and vetor[filho_direita] > vetor[pai]:
        # se o filho à direita maior do que a atual raiz, devem ser invertidos
        vetor[pai], vetor[filho_direita] = vetor[filho_direita], vetor[pai]
        # recursivamente ordena a subarvore à direita
        max_heapfy(vetor, filho_direita, tamanho)


def heap(vector):
    """
    Função principal do heap sort que ordenado um vetor de elementos
    comparáveis entre si.

    Args:
        vector: Iterável para ser ordenado.

    Returns:
        - Iterável com os elementos ordenados.
    """
    tamaho = len(vector) - 1

    # deixa o vetor com as propriedade de um max heap
    for i in range(tamaho//2, -1, -1):
        max_heapfy(vector, i, tamaho)

    for i in range(tamaho, 0, -1):
        # para cada elemento do vetor, o maior elemento (indice 0)
        # é colocado ao final, e o elemento do final vai para o inicio
        vector[0], vector[i] = vector[i], vector[0]

        # deixa o subvetor de 0 até a posicao atual-1 com as propriedades
        # de um max heap
        max_heapfy(vector, 0, i-1)

    return vector
