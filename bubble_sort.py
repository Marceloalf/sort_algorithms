def bubble(vector):
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
