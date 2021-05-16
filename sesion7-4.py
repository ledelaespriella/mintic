"""
debe realizar un muestreo con N personas para determinar 
el promedio de peso de los niños, jóvenes, adultos y viejos 
que existen en su zona habitacional.   Se determinan las categorías así:
		CATEGORIA			EDAD
		Niños				0 - 12
		Jóvenes				13 - 29
		Adultos				30 - 59
		Viejos				60 en adelante
"""

#ingreso de datos y definicion de variables

#defino variable para contar el total de personas por categorias
total_niños=0
total_jovenes=0
total_adultos=0
total_viejos=0   
#defino variable para sumar los pesos por categoria
peso_niños=0
peso_jovenes=0
peso_adultos=0
peso_viejos=0 
cuenta=1
n=int(input("Por favor ingrese la cantidad de personas a encuestar: "))
#procesamiento de datos
while cuenta<=n:
    edad=int(input("Por favor ingrese su edad: "))
    peso=float(input("Por favor ingrese su peso: "))
    print("\n")
    if edad>=0 and edad<=12:
        peso_niños=peso_niños+peso
        total_niños=total_niños+1
        cuenta=cuenta+1
    elif edad>=13 and edad<=29:
        peso_jovenes=peso_jovenes+peso
        total_jovenes=total_jovenes+1
        cuenta=cuenta+1
    elif edad>=30 and edad<=59:
        peso_adultos=peso_adultos+peso
        total_adultos=total_adultos+1
        cuenta=cuenta+1
    elif edad>=60:
        peso_viejos=peso_viejos+peso
        total_viejos=total_viejos+1
        cuenta=cuenta+1
        
#salida de datos

if total_niños>0:
    promedio_niños=peso_niños/total_niños
    print("El peso promedio de los niños es:",promedio_niños)

if total_jovenes>0:
    promedio_jovenes=peso_jovenes/total_jovenes
    print("El peso promedio de los jovenes es:",promedio_jovenes)

if total_adultos>0:
    promedio_adultos=peso_adultos/total_adultos
    print("El peso promedio de los adultos es:",promedio_adultos)

if total_viejos>0:
    promedio_viejos=peso_viejos/total_viejos
    print("El peso promedio de los adultos es:",promedio_viejos)
print("\n")  
print("Gracias por participar en la encuesta")