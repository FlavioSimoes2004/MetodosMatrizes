import numpy as np

matriz = [[1.0, 0.0, 0.0, 1.0, 35.0], [1.0, 1.0, 0.0, 0.0, 40.0], [0.0, 1.0, 1.0, -1.0, 30.0]]
def solucao(matriz):
    x = []
    a = []
    b = []
    for i in matriz:
        a.append(i[:len(matriz)])
    for i in matriz:
        b.append(i[-1])
    for pos, i in enumerate(matriz):
        x.append(b[pos]/i[pos])
    
    max_iter = 100
    for i in range(0, max_iter):
        print('vetor x atual: ', x, ' iteracao: ', i)
        xk_1 = np.asarray(x)            
        x = np.asarray(seidel(a, x, b)) 
        if np.max(np.abs(x-xk_1))/np.max(np.abs(x)) < 10**(-2):
            print('Convergencia: ', np.max(np.abs(x-xk_1))/np.max(np.abs(x)), ' vetor x atualizado: ', x)
            break
        print('vetor x atualizado: ', x)
    
def seidel(a, x ,b):        
    n = len(a)              
    for j in range(0, n):         
        d = b[j]                   
        for i in range(0, n):    
            if(j != i): 
                d-=a[j][i] * x[i]
        x[j] = d / a[j][j]
    return x