"""
Haga un programa que permita capturar
una lista de n numeros y al final me calcule y me muestre
el promedio de los numeros.
"""
promedio=0
acumulado=0
cuenta=1
n=int(input("cuantos numeros son? :"))
while cuenta<=n:
    numero=float(input("Numero:"))
    acumulado=acumulado + numero
    print("la sumatoria hasta el momento es ",acumulado)
    cuenta=cuenta+1

promedio=acumulado/n
print("El promedio general de la lista de Numeros es ",promedio)