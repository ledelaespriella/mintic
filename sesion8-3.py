"""
Ejercicio2:
En una empresa de ventas masiva se desea desarrollar
una aplicacion que permita generar ciertos informes de ventas
teniendo en cuenta la siguinte informacion:
a)existen N sucursales de la empresa(nombre sucursal, codigo
sucursal, direccion)
b)en cada sucursal hay N vendedores(nombres, codigos de vendedores)
cada vendedor realiza N ventas en cada meses del primer semestre
del año.
(N ventas por mes)

se desean arrojar los siguientes reportes:
- total de ventas por sucursal x
- total de ventas por vendedor x
- total de ventas por mes x
- total de ventas de todo el semestre x
- Promedio de ventas por sucursal x
- promedio de ventas por vendedor x
- promedio de ventas por mes x
- promedio de ventas de todo el semestre  x

"""


num_sucursales=int(input("Por favor ingresa el numero de sucursales de la empresa: "))
c_1=1
while c_1<=num_sucursales:
    nombre_sucursal=input("Ingrese el nombre de la suscural "+str(c_1)+":")
    codigo_sucursal=int(input("Ingrese el codigo de la sucursal "+str(c_1)+":"))
    direccion_sucursal=input("Ingresa la direccion de la sucursal "+str(c_1)+":")
    num_vendedores=int(input("Ingrese el numero de vendedores de la sucursal "+str(c_1)+":"))
    c_2=1
    acum_sucursal=0
    while c_2<=num_vendedores:
        nombre_vendedor=input("Ingrese el nombre del vendedor "+str(c_2)+":")
        codigo_vendedor=int(input("Ingrese el codigo del venderdor "+str(c_2)+":"))
        c_3=1
        acum_total_mes=0
        while c_3<=6:
            num_ventas=int(input("Ingrese el numero de ventas que "+nombre_vendedor+" llevo a cabo en la sucursal "+str(c_1)+" En el mes "+str(c_3)+":"))
            c_4=1
            acum_venta_mes=0
            while c_4<=num_ventas:
                venta=int(input("Ingrese el valor de la venta "+str(c_4)+":"))
                acum_venta_mes+=venta
                c_4+=1
            print("El total de ventas de "+str(nombre_vendedor)+" en el mes "+str(c_3)+" fue:",acum_venta_mes)
            promedio_ventas_mes=acum_venta_mes/num_ventas
            print("El promedio de ventas de "+str(nombre_vendedor)+" en el mes "+str(c_3)+" es:",promedio_ventas_mes)
            acum_total_mes+=acum_venta_mes
            c_3+=1
        print("El total de ventas del semestre de "+str(nombre_vendedor)+" en la suscursal "+str(c_1)+" fue de: ",acum_total_mes)
        promedio_ventas_vendedor=acum_total_mes/6
        print("El promedio de ventas de "+str(nombre_vendedor)+" en la sucural "+str(c_1)+" durante el semestre fue: ",promedio_ventas_vendedor)
        acum_sucursal+=acum_total_mes
        c_2+=1
    print("El total de ventas de la sucursal "+str(nombre_sucursal)+" fue de: ",acum_sucursal)
    promedio_ventas_sucursal=acum_sucursal/num_vendedores
    print("El promedio de ventas de la sucursal "+str(nombre_sucursal)+" es de:",promedio_ventas_sucursal)
    c_1+=1
    