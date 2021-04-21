def bubble(vector):
    n = len(vector)
    if n < 1:
        return
    for j in range(n-1, 0, -1):
        for i in range(j):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux

    return vector


v = [i for i in range(10, -1, -1)]
print(bubble(v))
