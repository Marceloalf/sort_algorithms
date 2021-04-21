def intercal(p, q, r, vector):
    w = [0 for i in range(r - p)]

    for i in range(p, q):
        w[i - p] = vector[i]

    for j in range(q, r):
        w[r - p + q - j - 1] = vector[j]

    i, j = 0, r - p - 1
    for k in range(p, r):
        if w[i] <= w[j]:
            vector[k] = w[i]
            i += 1
        else:
            vector[k] = w[j]
            j -= 1


def merge(p, r, vector):
    if p < r - 1:
        q = int((p + r)/2)

        merge(p, q, vector)
        merge(q, r, vector)
        intercal(p, q, r, vector)

    return vector


v = [i for i in range(10, -1, -1)]
print(merge(0, len(v), v))

