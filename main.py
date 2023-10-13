import numpy as np
import Seidel, Gauss, Jacobi, Jordan

matriz = [[3.0, -2.0, 5.0, 20.0], [6.0, -9.0, 12.0, 51.0], [-5.0, 0, 2.0, 1.0]]

def main():
    printTxt = "1 - Gauss\n2 - Jordan\n3 - Jacobi\n4 - Seidel\n5 - FECHA"
    Options = ["1", "2", "3", "4", "5"]
    while True:
        matrizCopy = matriz.copy()
        print(printTxt)
        entrada = '1'
        while entrada not in Options:
            print("Entrada invalida\n")
            entrada = input()
        
        if entrada == "1":
            print("Gauss")
            Gauss.gaussianElimination(matrizCopy)
        elif entrada == "2":
            print("Jordan")
        elif entrada == "3":
            print("Jacobi")
        elif entrada == "4":
            print("Seidel")
            Seidel.solucao(matrizCopy)
        else:
            print("FECHANDO")
            break
        print("")

main()
