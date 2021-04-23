"""
insertion_sort.py
Author: Luan Rodrigues, Marcelo Augusto

Função que implementa o algoritmo de ordenação Insertion Sort em Python.

Para maiores intruções sobre as funções, veja as docstrings de cada função
separada.
------
Uso:
------
>>> from insertion_sort import insertion
>>> vetor_desordenado = [5, 1, 2, 10, 4]
>>> vetor_ordenado = insertion(x)
>>> print(vetor_ordenado)
[1, 2, 4, 5, 10]
"""


def insertion(vector):
    """
    Função principal do insertion sort que ordena o vetor fornecido.

    Args:
        vector: Iterável para ser ordenado.

    Returns:
        - Iterável com os itens ordenados entre si.
    """
    tamanho = len(vector)
    for i in range(tamanho):
        atual = vector[i]

        j = i - 1
        # enquanto existir algum elemento maior do que o
        # atual na parte do vetor já ordenado
        # (do atual para trás), os elementos são deslocado
        # para a direita
        while j >= 0 and vector[j] > atual:
            vector[j + 1] = vector[j]
            j = j - 1

        # adiciona o elemento atual na posição certa
        # (não existe nenhum elemeno menor a esqeurda do j
        vector[j + 1] = atual

    return vector
