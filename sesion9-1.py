"""

for i in range(1,5):
    print("Hola mundo "+str(i))
print("Fin del ciclo")

"""
"""
n=int(input("Por favor ingrese la cantidad de notas: "))
suma=0
for c_1 in range(1,n+1):
    nota=float(input("Ingrese la nota "+str(c_1)+":"))
    suma+=nota
    c_1+=1

prom=suma/n
print("El prmomedio es: ",prom)

"""

for i in [10,20,30,40,50]:
    print("mostrar ",i)
    
for ciudad in ["Cartagena","Barranquilla"]:
    print(ciudad)

for letra in "ingrese la ciudad: ":
    print(letra)
    
    