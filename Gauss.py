import numpy as np

def gauss(A, b):
    n = len(A) #tamanho da matriz A
    x = [0] * n
    x = np.asarray(x)
    count = 0

    for i in range(n):
        # Achar o elemento de maior valor presente na coluna atual
        max_index = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        A = trocarLinha(A, i, max_index)
        b = trocarLinha(b, i, max_index)
        count += 1

        for j in range(i+1, n):
            fator = A[j][i] / A[i][i]
            A[j] -= A[i].dot(fator)
            b[j] -= b[i].dot(fator)
            count += 1

    # Substituição de volta
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    print("interactions: ", count)
    return x

def trocarLinha(mat, i ,j):
    aux = mat[i]
    mat[i] = mat[j]
    mat[j] = aux
    return mat