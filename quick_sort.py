def separa(inicio, fim, vector):
    """
    Seprar o vetor de modo que o dado um índice J, todos os elemetos
    a direita são maiores todos a esquerda são menores. Ao final é retornado
    o índice com essas propriedades
    """
    pivo = vector[inicio]
    i = inicio + 1  # ponteiro para os elementos menores do que o pivô
    j = fim  # ponteiro para os elementos maiores do que o pivô

    while i <= j:  # enquanto ainda puder existir algum menor ou maior
        if vector[i] <= pivo:
            # move o ponteiro dos menores para posição seguinte até achar um maior
            i += 1
        elif pivo < vector[j]:
            # move o ponteiro dos maiores para posição seguinte até achar um menor
            j -= 1
        else:
            # ambos ponteiros, menor e maior encontraram um elemento do lado do vetor
            # errado, portanto deve-se trocar:
            #   o elememento maior (indicador por i) deve ir para direita
            #   o elemento menor (indicado por j) deve ir para esquerda
            aux = vector[i]
            vector[i] = vector[j]
            vector[j] = aux

    # após seperar os elementos menores para esquerda, e os maiores para a direita
    # é trocado o pivo com a posicao do meio, dessa forma o pivo já está na posicao correta
    aux = vector[inicio]
    vector[inicio] = vector[j]
    vector[j] = aux

    # retonar a posição do pivô
    return j


def quick(vector, inicio=0, fim=None):
    if fim is None:
        fim = len(vector) - 1

    if inicio < fim:
        pivo = separa(inicio, fim, vector)
        quick(vector, inicio, pivo - 1)
        quick(vector, pivo + 1, fim)

    return vector
