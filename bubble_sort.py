"""
bubble_sort.py
Author: Luan Rodrigues, Marcelo Augusto

Função que implementa o algoritmo de ordenação Bubble Sort em Python.

Para maiores intruções sobre as funções, veja as docstrings de cada função
separada.
------
Uso:
------
>>> from bubble_sort import bubble
>>> vetor_desordenado = [5, 1, 2, 10, 4]
>>> vetor_ordenado = bubble(x)
>>> print(vetor_ordenado)
[1, 2, 4, 5, 10]
"""


def bubble(vector):
    """
    Função principal do bubble sort que ordena o vetor fornecido.

    Args:
        vector: Iterável para ser ordenado.

    Returns:
        - Iterável com os itens ordenados entre si.
    """
    tamanho = len(vector)
    if tamanho < 1:
        # somente 1 elemento significa vetor ordenado
        return vector

    for j in range(tamanho-1, -1, -1):
        # percorre cada elemento do vetor

        for i in range(j):
            # percorre todos os elementos restantes para
            # comparar e trocas as posições
            if vector[i] > vector[i + 1]:
                # elemento da esquerda maior do que a direita, ou seja,
                # elemento da esquerda deve ir para a direita
                vector[i], vector[i + 1] = vector[i + 1], vector[i]

    return vector
