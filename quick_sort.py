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


def quick(vector, p=0, r=None):
    if r is None:
        r = len(vector) - 1

    if p < r:
        j = separa(p, r, vector)
        quick(vector, p, j - 1)
        quick(vector, j + 1, r)

    return vector
