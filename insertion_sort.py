def insertion(vector):
    n = len(vector)
    for i in range(n):
        eleito = vector[i]
        j = i - 1

        while (j >= 0) and (vector[j] > eleito):
            vector[j + 1] = vector[j]
            j = j - 1
        vector[j + 1] = eleito

    return vector


v = [i for i in range(10, -1, -1)]
print(insertion(v))
