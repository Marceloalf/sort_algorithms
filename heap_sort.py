def max_heapfy(vetor, pai, tamanho):
    filho_esquerda = pai * 2 + 1
    filho_direita = pai * 2 + 2

    if filho_esquerda <= tamanho and vetor[filho_esquerda] > vetor[pai]:
        vetor[pai], vetor[filho_esquerda] = vetor[filho_esquerda], vetor[pai]
        max_heapfy(vetor, filho_esquerda, tamanho)

    if filho_direita <= tamanho and vetor[filho_direita] > vetor[pai]:
        vetor[pai], vetor[filho_direita] = vetor[filho_direita], vetor[pai]
        max_heapfy(vetor, filho_direita, tamanho)


def heap(vector):
    n = len(vector) - 1

    for i in range(n//2, -1, -1):
        max_heapfy(vector, i, n)

    for i in range(n, 0, -1):
        vector[0], vector[i] = vector[i], vector[0]
        max_heapfy(vector, 0, i-1)

    return vector
