import numpy as np
import Seidel, Gauss

matriz = [[3, 2, 4, 1], [1, 1, 2, 2], [4, 3, -2, 3]]

def getB(matriz):
    b = []

    for i in range(matriz.__len__()):
        b.append([matriz.pop()])

    return b

def main():
    printTxt = "1 - Gauss\n2 - Seidel\n3 - FECHA"
    Options = ["1", "2", "3"]
    while True:
        matrizCopy = matriz.copy()
        print(printTxt)
        entrada = input()
        while entrada not in Options:
            print("Entrada invalida\n")
            entrada = input()
        
        if entrada == "1":
            Gauss.gauss(matrizCopy)
        elif entrada == "2":
            Seidel.solucao(matrizCopy)
        else:
            print("FECHANDO")
            break
        print("")

main()
