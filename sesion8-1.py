"""
Haga un programa que permita generar por cada numero
que se capture su numero factorial de los N numeros
pedidos
"""
n=int(input("Ingrese la cantidad de numeros a procesar: "))
conteo=1
while conteo<=n: #
    numero=int(input("Ingrese el numero: "))
    x=1
    factorial=1
    while x<=numero:
        factorial=factorial*x
        x+=1
    print("El factorial de",numero,"es",factorial)
    conteo+=1
print("Ha terminado de calcular los factoriales")
