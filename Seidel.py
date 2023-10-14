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
    max_iter = 25
    for i in range(0, max_iter):             
        x = seidel(a, x, b) 
        print(x)  
    
def seidel(a, x ,b):        
    n = len(a)                    
    for j in range(0, n):         
        d = b[j]                   
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i] 
        x[j] = d / a[j][j]            
    return x