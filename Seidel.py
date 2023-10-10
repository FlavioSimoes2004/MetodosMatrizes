import numpy as np

def solucao(matriz):
    size = len(matriz)
    matResult = []

    for i in range(size):
        matResult.append(matriz[i][matriz[i].__len__() - 1])
        matriz[i].pop()
    
    matriz = np.asarray(matriz)
    matResult = np.asarray(matResult)
    x0 = np.zeros_like(b, dtype=float)
    gauss_seidel(matriz, matResult, x0)

def gauss_seidel(A, b, x0, tol=10e-7, max_iter=100):
    n = len(b)
    x = x0.copy()
    iters = 0
    
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        
        residual = np.abs(b - np.dot(A, x_new))
        
        if np.all(residual < tol):
            break
        
        x = x_new
        iters += 1
    
    return x, iters

# Exemplo de uso: x = 1, y = 2
A = np.array([[1, 2], [2, 4]], dtype=float)
b = np.array([5, 10], dtype=float)
x0 = np.zeros_like(b, dtype=float)

#solution, iterations = gauss_seidel(A, b, x0)
