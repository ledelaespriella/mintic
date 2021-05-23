"""

ejercicio2:
haga un programa que capture un texto cualquiera y haga lo 
siguiente:
1)contar la cantidad de vocales mayusculas y/o minusculas
  que encontro
2)contar las consonantes mayusculas y/o minusculas que 
encontro
3) contar los simbolos especiales que encontro
4)informar cual fue la mayor busqueda

"""

texto=input("Digite la palabra: ").lower()
c_vocales=0
c_cons=0
con_especial=0
import string

for i in texto:
    if (i.isalpha()==True):
        if i=="a" or i=="A":
            c_vocales+=1
        elif i=="e" or i=="E":
            c_vocales+=1
        elif i=="i" or i=="I":
            c_vocales+=1
        elif i=="o" or i=="O":
            c_vocales+=1
        elif i=="u" or i=="U":
            c_vocales+=1
        else:
            c_cons+=1
    else:
        for j in list(string.punctuation):
            if (i==j):
                con_especial+=1
            
print("Las vocales encontradas son:",c_vocales)
print("Las consonantes encontradas son:",c_cons)
print("Los caracteres espacieles encontrados son: ",con_especial)
mayor=0
if c_vocales>=c_cons and c_vocales>=con_especial:
    mayor=c_vocales
elif c_cons>=c_vocales and c_cons>=con_especial:
    mayor=c_cons
else:
    mayor=con_especial

