def intercala(inicio, meio, fim, vector):
    w = [0 for i in range(fim - inicio)]

    for i in range(inicio, meio):  # adiciona os dados da esquerda ao vetor aux
        w[i - inicio] = vector[i]

    for j in range(meio, fim):  # adiciona os dados da direita ao vetor aux
        w[fim - inicio + meio - j - 1] = vector[j]

    i, j = 0, fim - inicio - 1  # ponteiros para marca posicoes da esquerda e direita
    # i = ponteiro para posicao do lado esquerdo
    # j = ponteiro para posicao do lado direito

    for k in range(inicio, fim):  # loop em todos os itens para juntar esquerda + direita
        if w[i] <= w[j]:
            # se o atual da esquerda for o menor, então adiciona ao vetor
            vector[k] = w[i]
            i += 1
        else:
            # se o atual da direita for o menor, então adiciona ao vetor
            vector[k] = w[j]
            j -= 1


def merge(vector, inicio=0, fim=None):
    if fim is None:
        fim = len(vector)

    if inicio < fim - 1:
        meio = (inicio + fim) // 2  # divide o vetor em duas partes iguais

        merge(vector, inicio, meio)  # ordena recusivamente a metadre da esquerda
        merge(vector, meio, fim)  # ordena recurvivamente a metade da direita
        intercala(inicio, meio, fim, vector)  # junta ambas as partes ordenadas

    return vector

