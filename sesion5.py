"""
Cada ejemplo y actividad será definida como un bloque independiente.
Si-Sino-Finsi
Recuerda que los condicionales múltiples y anidados nos permiten evaluar múltiples casos. 
El condicional Si-Sino-Si-Finsi tiene la siguiente estructura:

    Si (condición) Entonces
        instrucción(es)
    Sino Si
        instrucción(es)
    Fin Si

En Python, esto se escribe un poco diferente y la estructura general depende de las tabulaciónes. 
Por ejemplo:
"""
def ejemplo1():
    x = int(input("Por favor ingresa un número: "))
    if x < 0:
        print('El número es Negativo')
    elif x > 0:
        print('El número es positivo')
    elif x == 0:
        print('El número es cero')
ejemplo1()

def actividad1():
    x=input("¿Cual es la luz del semaforo (V, A, R)?: ")
    verde="Siga"
    amarillo="Precaución"
    rojo="Pare"
    if x=="V":
        print(str(verde))
    elif x=="A":
        print(str(amarillo))
    elif x=="R":
        print(str(rojo))
print(actividad1())


    #Escribe el código que imprima un comando dada la luz del semáforo
        #Verde = Siga
        #Amarillo = Precaución
        #Rojo = Pare

# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
#actividad1()

def actividad2():
    
    x=input("¿Cual es la luz del semaforo (V, A, R)?: ")
    verde="Siga"
    amarillo="Precaución"
    rojo="Pare"
    if x=="V":
        print(str(verde))
        peaton=input("¿Hay algun petaton? (SI/NO): ")
        if peaton=="SI":
            print("Pare")
        else:
            print("siga")
    elif x=="A":
        print(str(amarillo))
        peaton=input("¿Hay algun petaton? (SI/NO): ")
        if peaton=="SI":
            print("Pare")
        else:
            print("precaucion")
    elif x=="R":
        print(str(rojo))

    
    #Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peaton o no (hayPeaton), imprima:
        #Verde -------- Si hay peaton - Pare, Sino - Siga
        #Amarillo ----------- Si hay peaton - Pare, Sino - Precaución
        #Rojo = Pare

actividad2()

def actividad3():
    print("Escriba dos numeros")
    a=int(input("Valor 1: "))
    b=int(input("Valor 2: \n"))
    suma=a+b
    multiplicacion=a*b
    resta=a-b
    division=a/b
    print("Ahora escoga entre las siguientes opciones")
    print("opcion 1 para sumar")
    print("opcion 2 para multiplicar")
    print("opcion 3 para restar valor 1 - varlor 2")
    print("opcion 4 para dividir valor 1 / valor 2\n")
    opcion=int(input("opcion: "))
    if opcion==1:
        print("el resultado de la suma es: ",suma)
    elif opcion==2:
        print("el resultado de la multiplicacion es: ",multiplicacion)
    elif opcion==3:
        print("el resultado de la resta es: ",resta)
    elif opcion==4:
        print("el resultado de la division es: ",division)
    
    print(actividad3)
    #Escribe el código para dos numeros a y b, el usuario va a seleccionar una opcion: 
        #1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y 
        #retornar el resultado de la operación indicada.


#actividad3()