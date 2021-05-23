numero = 4987
maximo_final = numero
numero_temp = numero
numero_nuevo = ""
if (numero <= 0):
    print("Ingrese un numero mayor a 0")
else:
    print("El numero inicialmente es", numero)
    while (numero != 0):
        digito = numero % 10 # encontramos el digito menos significativos de numero
        maximo_numero = digito # va a llevar memoria de cual es el MAX digito hasta el momento
        numero_temp = numero // 10 # asignamos a numero_temp el numero sin el digito menos significativo
        posicion = 0
        while (numero_temp != 0):
            digito_temp = numero_temp % 10
            numero_temp = numero_temp // 10
            if (digito_temp > maximo_numero):
                posicion = posicion + 1
                maximo_numero = digito_temp
        numero_nuevo = numero_nuevo + str(maximo_numero)
        if (posicion == 0):
            numero = numero // 10
        else:
            numeros_antes = str(numero % 10**posicion)
            numeros_despues = str(numero // 10**(posicion+1))
            if (numeros_despues == "0"):
                numeros_despues = ""
            numero = int(numeros_despues+numeros_antes)
    print("El nuevo numero es", numero_nuevo)