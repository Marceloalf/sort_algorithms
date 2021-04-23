def intercala(inicio, meio, fim, vector):
    esquerda = vector[inicio:meio]  # metade a esquerda do meio
    direita = vector[meio:fim]  # metade a direita do meio, incluindo

    i, j = 0, 0
    # i = indice que aponta para posição atual do vetor da esquerda
    # j = indice que aponta para posição atual do vetor da direita
    for k in range(inicio, fim):
        if i < len(esquerda) and esquerda[i] <= direita[j]:  # elemento da esquerda é menor
            vector[k] = esquerda[i]
            i += 1  # incremento da posição atual da esquerda
        else:
            vector[k] = direita[j]  # elemento da direita é menor
            j += 1  # incremento da posição atual da direita


def merge(vector, inicio=0, fim=None):
    if fim is None:
        fim = len(vector)

    if inicio < fim - 1:
        meio = (inicio + fim) // 2  # divide o vetor em duas partes iguais

        merge(vector, inicio, meio)  # ordena recusivamente a metadre da esquerda
        merge(vector, meio, fim)  # ordena recurvivamente a metade da direita
        intercala(inicio, meio, fim, vector)  # junta ambas as partes ordenadas

    return vector
