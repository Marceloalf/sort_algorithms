def heapfy(vector, m):
    for k in range(1, m):
        f = k + 1

        while f > 1 and vector[f // 2] < vector[f]:
            aux = vector[f // 2]
            vector[f // 2] = vector[f]
            vector[f] = aux

            f = f // 2


def sieve(p, m, vector):
    f = 2

    while f <= m:
        if f < m and vector[f] < vector[f + 1]:
            f += 1

        if vector[p] >= vector[f]:
            break

        aux = vector[p]
        vector[p] = vector[f]
        vector[f] = aux

        p = f
        f = 2 * p


def sieve2(p, m, vector):
    f = 2 * p

    if f <= m:
        if f < m and vector[f] < vector[f + 1]:
            f += 1

        if vector[p] >= vector[f]:
            return

        aux = vector[p]
        vector[p] = vector[f]
        vector[f] = aux

        sieve2(f, m, vector)


def heap(vector):
    n = len(vector) - 1

    heapfy(vector, n)
    for i in range(n, 1, -1):
        aux = vector[0]
        vector[0] = vector[i]
        vector[i] = aux

        sieve2(0, i - 1, vector)

    return vector


v = [2, 3, 5, 1, 3, 4, 1, 2]
print(v)
print(heap(v))
