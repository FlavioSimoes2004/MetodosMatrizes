import numpy as np
import Seidel, Gauss

matriz = [[1.0, 0.0, 0.0, 1.0, 35.0], [1.0, 1.0, 0.0, 0.0, 40.0], [0.0, 1.0, 1.0, -1.0, 30.0]]

def getB(matriz):
    b = []

    for i in range(matriz.__len__()):
        b.append([matriz[i].pop()])

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
            b = getB(matrizCopy)
            print(Gauss.eliminacao_de_gauss(np.asarray(matrizCopy), np.asarray(b)))
        elif entrada == "2":
            Seidel.solucao(matrizCopy)
        else:
            print("FECHANDO")
            break
        print("")

main()