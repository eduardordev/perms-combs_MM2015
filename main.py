#UNIVERSIDAD DEL VALLE DE GUATEMALA
#MATEMATICA DISCRETA - MM2015
#PROYECTO FINAL
#EDUARDO RAMÍREZ HERRERA #19946
#MARTIN ESPAÑA #19258
import itertools
from itertools import *

print("")
print("/=========================================\ ")
print("|************ PROYECTO FINAL *************|")
print("|********** MATEMATICA DISCRETA **********|")
print("|***** PERMUTACIONES Y COMBINACIONES *****|")
print("\=========================================/\n")

state1 = True
state2 = True

while(state1):

    state2 = True
    count = 0 #contador para llenar el conjunto

    max = int(input("Escriba la cantidad maxima de elementos en su conjunto: "))
    print("------------------------------------------")

    a = [] #Lista contenedora del conjunto

    #Bucle while para llenar el conjunto
    while count < max:
        n = input("Ingrese una letra o un numero a su conjunto: ")
        a.append(n)
        count += 1
    print("------------------------------------------")

    k = int(input("Escriba la cantidad k de elementos que desea seleccionar del conjunto: "))

    print("------------------------------------------")
    print("Los valores del conjunto son: ")
    print(a)
    print("------------------------------------------")

    while state2:

        print("1. PERMUTACION ")
        print("2. COMBINACION ")
        print("3. AMBAS ")
        print("4. SALIR ")
        print("------------------------------------------")
        opt = int(input("Elija la opcion que desea realizar: "))
        print("------------------------------------------")

        if opt == 1:
            print("***** PERMUTACIONES *****\n")

            per = list(itertools.permutations(a, k))
            print(per)
            print("------------------------------------------")
            print("Cantidad de permutaciones: ")
            pc = len(set(per))
            print(pc)
            print("")

            print("------------------------------------------")

        if opt == 2:
            print("***** COMBINACIONES *****\n")

            cmb = list(itertools.combinations(a, k))
            print(cmb)
            print("")

            print("------------------------------------------")
            print("Cantidad de combinaciones: ")
            cc = len(set(cmb))
            print(cc)
            print("------------------------------------------")

        if opt == 3:
            print("***** PERMUTACIONES Y COMBINACIONES *****\n")

            print("PERMUTACIONES: ")
            per = list(itertools.permutations(a, k))
            print(per)
            print("")

            print("------------------------------------------")
            print("Cantidad de permutaciones: ")
            pc = len(set(per))
            print(pc)
            print("")

            print("------------------------------------------")
            print("COMBINACIONES: ")
            cmb = list(itertools.combinations(a, k))
            print(cmb)
            print("")

            print("------------------------------------------")
            print("Cantidad de combinaciones: ")
            cc = len(set(cmb))
            print(cc)

            print("------------------------------------------")

        if opt == 4:
            state2 = False

    exit = input("Si desea salir del programa presione la tecla Y (o presione enter para continuar con un nuevo conjunto): ")
    print("------------------------------------------")

    if exit == "y" or exit == "Y":
        print("***** FIN DEL PROGRAMA *****")
        state1 = False
        break
