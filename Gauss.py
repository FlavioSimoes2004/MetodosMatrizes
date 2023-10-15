import numpy as np

def gauss(A, b):
    n = len(A) #tamanho da matriz A
    x = [0] * n
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
        #A[i], A[max_index] = A[max_index], A[i]
        #b[i], b[max_index] = b[max_index], b[i]
                

        for j in range(i+1, n):
            fator = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= fator * A[i][k]
            b[j] -= fator * b[i]
            count += 1

    # Substituição de volta
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    
    return x

def trocarLinha(mat, i ,j):
    aux = mat[i]
    mat[i] = mat[j]
    mat[j] = aux
    return mat