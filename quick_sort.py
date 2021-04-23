"""
quick_sort.py
Author: Luan Rodrigues, Marcelo Augusto

Conjunto de funções para implementar o algoritmo de ordenação
QuickSort em Python.

Para maiores intruções sobre as funções, veja as docstrings de cada função
separada.
------
Uso:
------
>>> from quick_sort import quick
>>> vetor_desordenado = [5, 1, 2, 10, 4]
>>> vetor_ordenado = quick(vetor_desordenado)
>>> print(vetor_ordenado)
[1, 2, 4, 5, 10]
"""


def separa(inicio, fim, vector):
    """
    Seprar o vetor de modo que o dado um índice J, todos os elemetos
    a direita são maiores todos a esquerda são menores. Ao final é retornado
    o índice com essas propriedades.

    Args:
        inicio: Ínidice do ínicio do vetor para aplicar a propriedade.
        fim: Índice do fim do vetor para aplicar a propriedade.
        vector: Iterável para ser ordenado.

    Returns:
        - int: Índice do pivô.
    """
    pivo = vector[inicio]
    i = inicio + 1
    # i = ponteiro para os elementos menores do que o pivô
    j = fim
    # j = ponteiro para os elementos maiores do que o pivô

    while i <= j:
        # enquanto ainda puder existir algum menor ou maior

        if vector[i] <= pivo:
            # move o ponteiro dos menores para posição
            # seguinte até achar um maior
            i += 1
        elif pivo < vector[j]:
            # move o ponteiro dos maiores para posição
            # seguinte até achar um menor
            j -= 1
        else:
            # ambos ponteiros, menor e maior encontraram um
            # elemento do lado do vetor errado,
            # portanto deve-se trocar:
            #   o elememento maior (indicador por i) deve ir para direita
            #   o elemento menor (indicado por j) deve ir para esquerda
            aux = vector[i]
            vector[i] = vector[j]
            vector[j] = aux

    # após seperar os elementos menores para esquerda, e os
    # maiores para a direita é trocado o pivo com a posicao do meio,
    # dessa forma o pivo já está na posicao correta
    aux = vector[inicio]
    vector[inicio] = vector[j]
    vector[j] = aux

    # retonar a posição do pivô
    return j


def quick(vector, inicio=0, fim=None):
    """
    Função principal do quick sort.

    Args:
        vector: Iterável para ser ordenado.
        inicio: Índice do início do vetor a ser ordenado.
        fim: Índice do fim do vetor a ser ordenado.

    Returns:
        - Iterável com os itens do `vetor` ordenado.
    """
    if fim is None:
        fim = len(vector) - 1

    if inicio < fim:
        pivo = separa(inicio, fim, vector)  # separad em 2
        quick(vector, inicio, pivo - 1)  # lado esquerdo
        quick(vector, pivo + 1, fim)  # lado direito

    return vector
