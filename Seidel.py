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
        #print each time the updated solution 
        print(x)  
    
def seidel(a, x ,b): 
    #Finding length of a(3)        
    n = len(a)                    
    # for loop for 3 times as to calculate x, y , z 
    for j in range(0, n):         
        # temp variable d to store b[j] 
        d = b[j]                   
        # to calculate respective xi, yi, zi 
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i] 
        # updating the value of our solution         
        x[j] = d / a[j][j] 
    # returning our updated solution            
    return x     



