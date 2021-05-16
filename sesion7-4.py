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
contador=1
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

#procesamiento de datos, el sistema ingresara cada individio
while cuenta<=n:
    edad=int(input("Por favor ingrese la edad del encuestado "+str(contador)+": "))
    peso=float(input("Por favor ingrese el peso en kg del encuestado "+str(contador)+": "))
    print("\n")
    if edad>=0 and edad<=12:
        peso_niños+=peso
        total_niños+=1
        cuenta+=1
        contador+=1
    elif edad>=13 and edad<=29:
        peso_jovenes+=peso
        total_jovenes+=1
        cuenta+=1
        contador+=1
    elif edad>=30 and edad<=59:
        peso_adultos+=peso
        total_adultos+=1
        cuenta+=1
        contador+=1
    elif edad>=60:
        peso_viejos+=peso
        total_viejos+=+1
        cuenta+=1
        contador+=1
    else:
        print=("Dato ingresado no valido para este sistema")
        contador=n
        
#salida de datos, por categoria

print("Los datos arrojan los siguiente resultados")
print("Categoria \t No. Encuestados \t Peso Promedio") #elaboro una tabla por categoria utilizando \t
if total_niños>0:
    promedio_niños=peso_niños/total_niños
    print("Niños \t\t\t",str(total_niños)+"\t\t\t",promedio_niños)
else:
    print("Niños \t\t\t\t",str(0)+"\t\t\t",0)

if total_jovenes>0:
    promedio_jovenes=peso_jovenes/total_jovenes
    print("Jovenes \t\t",str(total_jovenes)+"\t\t\t",promedio_jovenes)
else:
    print("Jovenes \t\t",str(0)+"\t\t\t",0)

if total_adultos>0:
    promedio_adultos=peso_adultos/total_adultos
    print("Adultos \t\t",str(total_adultos)+"\t\t\t",promedio_adultos)
else:
    print("Adultos \t\t",str(0)+"\t\t\t",0)

if total_viejos>0:
    promedio_viejos=peso_viejos/total_viejos
    print("Viejos \t\t\t",str(total_viejos)+"\t\t\t",promedio_viejos)
else:
    print("viejos \t\t\t",str(0)+"\t\t\t",0)

print("\n")  
print("Gracias por participar en la encuesta")
