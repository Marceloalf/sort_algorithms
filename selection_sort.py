"""
selection_sort.py
Author: Luan Rodrigues, Marcelo Augusto

Função que implementa o algoritmo de ordenação Selection Sort em Python.

Para maiores intruções sobre as funções, veja as docstrings de cada função
separada.
------
Uso:
------
>>> from selection_sort import selection_sort
>>> vetor_desordenado = [5, 1, 2, 10, 4]
>>> vetor_ordenado = selection_sort(x)
>>> print(vetor_ordenado)
[1, 2, 4, 5, 10]
"""


def selection_sort(vector):
    """
    Função principal do selection sort que ordena o vetor fornecido.

    Args:
        vector: Iterável para ser ordenado.

    Returns:
        - Iterável com os itens ordenados entre si.
    """
    n = len(vector)

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            # procura um elemento menor do que o atual
            if vector[j] < vector[i]:
                menor = j

        if i != menor:
            # se tiver encontrado um menor entao altera com o menor
            vector[i], vector[menor] = vector[menor], vector[i]

    return vector
