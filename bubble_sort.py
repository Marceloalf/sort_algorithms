def bubble(vector):
    tamanho = len(vector)
    if tamanho < 1:
        return

    for j in range(tamanho-1, 0, -1):
        for i in range(j):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux

    return vector
