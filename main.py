import numpy as np
import Seidel, Gauss, Jacobi, Jordan, Gauss2

matriz = [[3, 2, 4, 1], [1, 1, 2, 2], [4, 3, -2, 3]]

def getB(matriz):
    b = []

    for i in range(matriz.__len__()):
        b.append([matriz.pop()])

    return b

def main():
    printTxt = "1 - Gauss\n2 - Jordan\n3 - Jacobi\n4 - Seidel\n5 - FECHA"
    Options = ["1", "2", "3", "4", "5"]
    while True:
        matrizCopy = matriz.copy()
        print(printTxt)
        entrada = input()
        while entrada not in Options:
            print("Entrada invalida\n")
            entrada = input()
        
        if entrada == "1":
            print("Gauss")
            Gauss.gauss(matrizCopy)
        elif entrada == "2":
            print("Jordan")
        elif entrada == "3":
            b = getB(matrizCopy)
            x0 = np.zeros_like()
            Jacobi.gauss_jacobi(matrizCopy, b, x0)
        elif entrada == "4":
            Seidel.solucao(matrizCopy)
        else:
            print("FECHANDO")
            break
        print("")

main()
