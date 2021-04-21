def separa(p, r, vector):
    pivo, i = vector[p], p + 1
    j = r

    while i <= j:
        if vector[i] <= pivo:
            i += 1

        else:
            if pivo < vector[j]:
                j -= 1
            else:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux

    aux = vector[p]
    vector[p] = vector[j]
    vector[j] = aux

    return j


def quick(p, r, vector):
    if p < r:
        j = separa(p, r, vector)
        quick(p, j - 1, vector)
        quick(j + 1, r, vector)

    return vector


v = [i + 32 for i in range(100, -1, -1)]
print(quick(0, len(v) - 1, v))
