def selection_sort(vector):
    n = len(vector)

    for i in range(n):
        minimal = i
        for j in range(i + 1, n):
            if vector[j] < vector[i]:
                minimal = j

            if vector[i] != vector[minimal]:
                aux = vector[i]
                vector[i] = vector[minimal]
                vector[minimal] = aux

    return vector
