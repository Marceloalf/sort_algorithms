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


v = [i for i in range(10, -1, -1)]
print(selection_sort(v))
