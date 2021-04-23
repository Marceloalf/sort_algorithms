def insertion(vector):
    tamanho = len(vector)
    for i in range(tamanho):
        atual = vector[i]

        j = i - 1
        # enquanto existir algum elemento maior do que o atual na parte do vetor
        # já ordenado (do atual para trás), os elementos são deslocado
        # para a direita
        while j >= 0 and vector[j] > atual:
            vector[j + 1] = vector[j]
            j = j - 1

        # adiciona o elemento atual na posição certa (não existe nenhum elemeno menor
        # a esqeurda do j
        vector[j + 1] = atual

    return vector
