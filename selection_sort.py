def selection_sort(vector):
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
