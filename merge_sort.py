def intercala(inicio, meio, fim, vector):
    w = [0 for i in range(fim - inicio)]

    for i in range(inicio, meio):
        w[i - inicio] = vector[i]

    for j in range(meio, fim):
        w[fim - inicio + meio - j - 1] = vector[j]

    i, j = 0, fim - inicio - 1
    for k in range(inicio, fim):
        if w[i] <= w[j]:
            vector[k] = w[i]
            i += 1
        else:
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

