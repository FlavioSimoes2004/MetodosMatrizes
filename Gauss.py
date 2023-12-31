import numpy as np

def gauss(A, b, e=-3):
    erro = 10**e
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
        printIteraction(A, b)
        count += 1

        for j in range(i+1, n):
            fator = A[j][i] / A[i][i]
            if fator != 0 and abs(fator) < erro:
                print(fator)
                raise Exception("criterio parada")
            A[j] -= A[i].dot(fator)
            b[j] -= b[i].dot(fator)
            printIteraction(A, b)
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

def printIteraction(A, b):
    for i in range(A.__len__()):
        print(A[i], b[i])
    print('\n')