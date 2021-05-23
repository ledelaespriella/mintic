"""
ejercicio1:
haga un programa que permita generar las tablas de multiplicar
del rango de tablas que el usuario indique.
ej:
tabla inicial:5
tabla final:7

5x1=5
5x2=10
5x3=15
.
.
.
5x10=50
-----------
6x1=6
6x2=12
.
.
-----------
7x1=7
7x2=
.

"""
num_1=int(input("Ingrese la tabla inicial a calcular: "))
num_2=int(input("Ingrese la tabla final a calcular: "))
for c_1 in range(num_1,num_2+1):
  print("TABLA DEL "+str(c_1)+"\n")
  for c_2 in range(1,11):
    multip=c_1*c_2
    print(str(c_1)+"*"+str(c_2)+"= ",multip)
  print("\n")
