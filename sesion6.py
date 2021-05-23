""" 
Ejercicio 1
#ingreso de datos
compra=float(input("Ingrese el valor de la compra: "))
#procesamiento de datos
valor_descuento=compra*(1-0.20) #formula para hallar el valor con el 20% de descuento
if compra>200000:
    print("El valor a pagar es:",valor_descuento)
else:
    print("El valor a pagar es:",compra)
"""

"""
Ejercicio 2
#entrada de datos
mes=input("Ingrese el numero del mes para determinar cuantos dias tiene: ")
#procesamiento de datos
if mes=="1" or mes=="3" or mes =="5" or mes=="7" or mes=="8" or mes=="10" or mes=="12":
    print(31)
elif mes=="4" or mes=="6" or mes =="9" or mes=="11":
    print(30)
elif mes=="2":
    print(28,"o",29)
elif mes==str:
    print("Mes no valido")   
else:
    print("Mes no valido") 
    """
"""
Ejercicio 3

#entrada de datos
precio=float(input("Por favor ingrese el precio del kilo de manzana: "))
kilo=float(input("Por favor ingrese cuantos kilos lleva: "))
#procesamiento y salida de datos
subtotal=precio*kilo
if kilo>=0 and kilo<2:
    print("el valor a pagar es:",subtotal)
elif kilo>=2 and kilo<5:
    descuento=subtotal*(1-0.10)
    print("Usted tiene un descuento del 10 % por su compra")
    print("el valor a pagar es:",descuento)
elif kilo>=5 and kilo<10:
    descuento=subtotal*(1-0.15)
    print("Usted tiene un descuento del 15 % por su compra")
    print("el valor a pagar es:",descuento)
elif kilo>=10:
    descuento=subtotal*(1-0.20)
    print("Usted tiene un descuento del 20 % por su compra")
    print("el valor a pagar es:",descuento)
    
    """

"""Ejercicio 4

#entrada de datos
peso=float(input("Por favor ingrese su peso: "))
talla=float(input("Por favor ingrese su estatura en mts: "))
#procesamiento y salida de datos
imc=round(peso/(talla**2), 1)
print("su IMC es:",imc)
if imc>=18.5 and imc<24.9:
    print("clasificacion normal, riesgo promedio")
elif imc>=25.0 and imc<29.9:
    print("Tiene sobrepeso, riesgo Aumentado")
elif imc>=30.0 and imc<34.9:
    print("Tiene Obesidad grado I, riesgo Moderado")
elif imc>=35.0 and imc<39.9:
    print("Tiene Obesidad grado II, riesgo Severo")
elif imc>=40:
    print("Tiene Obesidad grado III, riesgo Muy severo")
    
"""

"""
Ejercicio 5
53.6
1.52 


#entrada de datos
ki=float(input("Por favor ingrese el km inicial: "))
kf=float(input("Por favor ingrese el km final recorrido: "))
#procesamiento y salida de datos
kr=kf-ki #defino los km recorridos
vr_pagar=300000 #defino el basico a pagar
if kr<=3000:
    print("El valor a pagar es",vr_pagar)
elif kr>3000 and kr<=10000:
    km_a_1=kr-3000 #establexco los km adicionales recorridos
    vr_a_pagar=km_a_1*150 #determino el valor adicional a pagar
    print("El valor a pagar es",vr_pagar+vr_a_pagar)
elif kr>10000:
    km_a_1=10000-3000 #establexco los km adicionales recorridos
    vr_a_pagar=km_a_1*150 #determino el valor adicional a pagar
    km_a_2=kr-10000
    vr_a_pagar_2=km_a_2*200
    print("El valor a pagar es",vr_pagar+vr_a_pagar+vr_a_pagar_2)
    
"""

"""EJERCICIO 6

valor_compra=float(input("Ingrese el valor de la compra: "))
if valor_compra>1000000:
    valor_pagar=valor_compra*(1-0.20)
    print("El valor de la compra tiene un descuento del 20%, el valor a pagar es: ",valor_pagar)
elif valor_compra==0 and valor_compra<=1000000:
    print("El valor a pagar es: ",valor_compra)
elif valor_compra<0:
    print("ERROR: datos invalidos")
    
"""

"""EJERCICIO 7

temp=float(input("Por favor ingrese la temperatura: "))
if temp>=(-10) and temp<10:
    print("Mucho firo")
elif temp>=10 and temp<15:
    print("Poco frio")
elif temp>=15 and temp<25:
    print("Temperatura normal")
elif temp>=25 and temp<30:
    print("Poco calor")
elif temp>=30 and temp<45:
    print("Mucho calor")

"""

"""
EJERCICIO 8

dia=int(input("Por fabor ingrese el día de la semana: "))
if dia==1:
    print("Lunes")
elif dia==2:
    print("Martes")
elif dia==3:
    print("Miercoles")
elif dia==4:
    print("Jueves")
elif dia==5:
    print("Viernes")
elif dia==6:
    print("Sabdado")
elif dia==7:
    print("Domingo")
else:
    print("ERROR")
    
"""

"""
EJERCICIO 9

utilidad=float(input("Por favor ingrese la utilidad anual: "))
tiempo=float(input("Por favor ingrese los años de antigüedad en la empresa: "))
if tiempo<1 and tiempo>=0:
    reparto=utilidad*0.05
    print("El reparto de utilidades, teniendo en cuenta su antigüedad de",f"{tiempo:.0f}","es de: ",reparto)
elif tiempo>=1 and tiempo<2:
    reparto=utilidad*0.07
    print("El reparto de utilidades, teniendo en cuenta su antigüedad de",f"{tiempo:.0f}","es de: ",reparto)
elif tiempo>=2 and tiempo<5:
    reparto=utilidad*0.1
    print("El reparto de utilidades, teniendo en cuenta su antigüedad de",f"{tiempo:.0f}","es de: ",reparto)
elif tiempo>=5 and tiempo<=10:
    reparto=utilidad*0.15
    print("El reparto de utilidades, teniendo en cuenta su antigüedad de",f"{tiempo:.0f}","es de: ",reparto)
elif tiempo>10:
    reparto=utilidad*0.25
    print("El reparto de utilidades, teniendo en cuenta su antigüedad de",f"{tiempo:.0f}","es de: ",reparto)
elif tiempo<0:
    print("ERROR, dato ingresado no valido")
    
"""

"""
EJERCICIO 10

ingresos=int(input("Por favor ingrese su salario: "))
vivienda=int(input("Por favor ingrese el valor de la vivienda: "))

if vivienda<122651010:
    if ingresos<1500000:
        cuota_inicial=vivienda*0.15
        mensualidad=(vivienda-cuota_inicial)/120
        print("Su cuota inicial es de: ",cuota_inicial)
        print("Su cuota es de: ",f"{mensualidad:.0f}")
    elif ingresos>=1500000:
        cuota_inicial=vivienda*0.30
        mensualidad=(vivienda-cuota_inicial)/(7*12)
        print("Su cuota inicial es de: ",cuota_inicial)
        print("Su cuota es de: ",f"{mensualidad:.0f}")
else:
    print("Esta vivienda no es VIS\nGracias por participar, este programa solo admite viviendas VIS")
"""
"""
EJERCICIO 11
"""
