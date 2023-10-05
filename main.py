import metGauss, metJacobi, metJordan, metSeidel

matriz = [[1, 2, 3], [4, 5, 6]]

def main():
    print("0- metodo Gauss")
    print("1- metodo Jacobi")
    print("2- metodo Jordan")
    print("3- metodo Seildel")
    t = input()
    while t != "0" and t != "1" and t != "2" and t != "3":
        print("entrada invalida")
        t = input()
    
    if t == "0":
        metGauss.findValues(matriz)
    elif t == "1":
        metJacobi.findValues(matriz)
    elif t == "2":
        metJordan.findValues(matriz)
    else: #t == 3
        metSeidel.findValues(matriz)


main()
print("")