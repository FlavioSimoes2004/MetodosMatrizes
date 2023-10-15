import numpy as np

def gauss(mat):
	gaussianElimination(mat)

def gaussianElimination(mat):
	global N
	N = mat[0].__len__() - 1 #pois a ultima coluna é o resultado da equacao
	#print("N = ", N)

	global iteraction
	iteraction = 0

	singular_flag = eliminar(mat)

	if (singular_flag != -1):
		print("Matriz Singular, tem um sistema inconscistente ou infinitas soluçoes")
		return

	backSub(mat)

def printMatriz(mat):
	iteraction += 1
	print("iteracao: ", iteraction)
	print(np.asarray(mat), "\n")

def trocarLinha(mat, i, j):

	for k in range(N + 1):
		temp = mat[i][k]
		mat[i][k] = mat[j][k]
		mat[j][k] = temp
	
	printMatriz(mat)

def eliminar(mat):
	for k in range(N):
	
		i_max = k
		v_max = mat[i_max][k]

		for i in range(k + 1, N):
			if (abs(mat[i][k]) > v_max):
				v_max = mat[i][k]
				i_max = i

		if not mat[k][i_max]:
			return k # Matrix e singular

		if (i_max != k):
			trocarLinha(mat, k, i_max)

		for i in range(k + 1, N):

			f = mat[i][k]/mat[k][k]

			for j in range(k + 1, N + 1):
				mat[i][j] -= mat[k][j]*f

			mat[i][k] = 0

			printMatriz(mat)

	return -1

def backSub(mat):

	x = [None for _ in range(N)] # array para armazenar a solucao

	for i in range(N-1, -1, -1):

		x[i] = mat[i][N]

		for j in range(i + 1, N):
		
			x[i] -= mat[i][j]*x[j]

		x[i] = (x[i]/mat[i][i])

	print("\nSolucao:")
	for i in range(N):
		print(x[i])