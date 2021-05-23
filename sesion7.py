"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

Por ejemplo:
"""

def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        i += 1
ejemplo1()

def actividad1():
    numero=float(input("Ingrese un numero: "))
    n=2
    while n<=numero:
        print(n)
        n=n+2
    print("Fin del ejercicio")
actividad1()
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número. 

# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
#actividad1()

def actividad2():
    numero=int(input("Diligencia el numero: "))
    cuenta=0
    while cuenta<numero:
        numero=numero/10
        cuenta=cuenta+1
    print("El numero de digitos es",cuenta)
actividad2()
    #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.

#actividad2()    
    

def actividad3():
    total_num=0
    promedio=0
    cuenta=0
    numero=int(input("Diligencia el numero: "))
    while numero!=-1:
        total_num+=numero
        cuenta+=1
        numero=int(input("Diligencia el numero: "))
    promedio=total_num/cuenta
    print("el promedio de todos los números ingresados hasta el momento es:",promedio)
actividad3()
    #Escribe el código que solicite números al usuario hasta que éste ingrese -1.
    #Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).

