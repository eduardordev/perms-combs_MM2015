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
    
    ##########################################################################################
    #Se solicita al usuario el número de elementos de su conjunto y se verifica que sea válido
    ##########################################################################################
    
    maxIncorrect = True
    
    while maxIncorrect:
        try:
            max = int(input("Escriba la cantidad maxima de elementos en su conjunto: "))
            if max > 0:
                print("------------------------------------------")
                maxIncorrect = False
            elif max <= 0:
                print("Debe ingresar un número no negativo mayor que 0...")
        except ValueError:
            print("Debe ingresar un número...")
    
    ##########################################################################################

    a = [] #Lista contenedora del conjunto

    #Bucle while para llenar el conjunto
    while count < max:
        n = input("Ingrese un elemento (letras o numeros) a su conjunto: ")
        a.append(n)
        count += 1
    print("------------------------------------------")
    
    ####################################################################
    #Se solicita al usuario el valor de k y se verifica que sea correcto
    ####################################################################
    
    kIncorrect = True

    while kIncorrect:
        try:
            k = int(input("Escriba la cantidad k de elementos que desea seleccionar del conjunto (-1 para mostrar todos):"))
        
            #El numero k es mayor o igual a 0 pero menor que el numero de elementos
            if k >= 0 and k < len(a):
                kIncorrect = False
            
            #El numero k es igual a (-1)
            elif k == -1:
                k = len(a)
                kIncorrect = False
            
            #El numero k es menor que (-1)
            elif k < -1:
                print("El número \"k\" debe ser mayor o igual a (-1)")
            
            #El numero k es mayor que el numero de elementos
            elif k > len(a):
                print("El número k debe ser menor o igual que el numero de elementos...")
                
        #El numero k no es una letra
        except ValueError:
            print("Debe ingresar un valor de \"k\" válido...")
    
    ####################################################################

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

        elif opt == 2:
            print("***** COMBINACIONES *****\n")

            cmb = list(itertools.combinations(a, k))
            print(cmb)
            print("")

            print("------------------------------------------")
            print("Cantidad de combinaciones: ")
            cc = len(set(cmb))
            print(cc)
            print("------------------------------------------")

        elif opt == 3:
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

        elif opt == 4:
            state2 = False

    exit = input("Si desea salir del programa presione la tecla (Y) (o presione enter para continuar con un nuevo conjunto): ")
    print("------------------------------------------")

    if exit == "y" or exit == "Y":
        print("***** FIN DEL PROGRAMA *****")
        state1 = False

