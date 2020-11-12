#UNIVERSIDAD DEL VALLE DE GUATEMALA
#MATEMATICA DISCRETA - MM2015
#PROYECTO FINAL
#EDUARDO RAMÍREZ HERRERA #19946
#MARTIN ESPAÑA #19258

print("------------------------------------------")
print("***** PERMUTACIONES Y COMBINACIONES *****")
print("------------------------------------------\n")

count = 0 #contador para llenar el conjunto

max = int(input("Escriba la cantidad maxima de elementos en su conjunto: "))
print("------------------------------------------")
a = [] #Lista contenedora del conjunto

#Bucle while para llenar el conjunto
while count < max:
    n = int(input("Ingrese un valor a su conjunto: "))
    a.append(n)
    count += 1

print("------------------------------------------")
print("Los valores del conjunto son: ")
print(a)
print("------------------------------------------")

print("1. PERMUTACION ")
print("2. COMBINACION ")
print("3. AMBAS ")
print("4. SALIR ")
print("------------------------------------------")
opt = input("Elija la opcion que desea realizar: ")
print("------------------------------------------")
