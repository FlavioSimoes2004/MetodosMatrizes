import numpy as np

def solucao(matriz):
    print("ok")

def gauss_jacobi(A, b, x0, max_iterations=100, tolerance=10e-6):
 def jacobi(a, b, x, n, tolerance):
    for k in range(n):
        next_x = [0, 0, 0]  # lista que armazena a próxima iteração
        for i in range(len(b)):
            bi = b[i]  # armazena o termo independente da linha i
            for j in range(len(b)):
                if j != i:
                    bi -= a[i][j] * x[j]  # multiplicar o valor das variáveis que não foram isoladas
            bi /= a[i][i]
            next_x[i] = bi

        # Verificar o critério de parada
        max_difference = max(abs(next_x[i] - x[i]) for i in range(len(b)))
        if max_difference < tolerance:
            print(f"Convergência alcançada na iteração {k + 1}")
            break

        x = next_x

    for i in range(len(b)):
        print(f'x_{i + 1} = {x[i]:.16f}\t')
        return next_x 

# Exemplo de uso
A = np.array([[4, 1, -1],
              [-1, 3, -1],
              [1, -1, 5]], dtype=float)
b = np.array([5, 6, 4], dtype=float)
x0 = [0, 0, 0]

#solution = gauss_jacobi(A, b, x0)
#print("Solução:", solution)