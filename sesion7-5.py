"""
2)En un supermercado un cajero captura los precios de los artículos 
que los clientes compran e indica a cada cliente cuál es el monto 
de lo que deben pagar.   
Al final del día le indica a su supervisor 
cuánto fué lo que cobró en total a todos los clientes 
que pasaron por su caja y cual fue el mayor monto de todos.

"""
"""
#entrada de datos y definicion de variables
cantidad_clientes=0
conteo=1

while conteo<=n:
    cliente=input("diligencia su nombre: ")
    totalproductos=1
    total_pagar=0
    p=0
    while p<=m:
        productos=input("Pruducto: ")
        cantidad=float(input("Cantidad: "))
        precio=float(input("Valor: "))
        vr_total_producto=precio*cantidad
        totalproducto=("El valor total por",productos,"es",vr_total_producto)
        print(totalproducto)
        p=p+1    
    total_pagar+=vr_total_producto
    
    print(cliente) 

"""
    
#establezco las variables
  
cliente, total, mayor = 0, 0, 0
#entrada de datos
entrada = input("Nuevo cliente (s/n): ")
while entrada=="S" or entrada=="s":
  cliente+=1
  suma=0
  productos=int(input("Cantidad de productos: " ))
  while productos > 0:
    nombre_producto=input("Nombre del producto: ")
    cantidad=int(input("Ingrese las cantidades del producto: "))
    valor = int(input("Ingresa el valor del producto:"))
    total_vr_p=cantidad*valor
    print("el total de",nombre_producto,"es",total_vr_p,"\n")
    suma += total_vr_p
    print("Su total hasta el momento es:",suma)
    if productos>0:
      descuento=input("Desea eliminar el producto (S o N): ")
      reinicio=0
      while descuento=="s" or descuento=="S":
        cantidad=int(input("Ingrese las cantidades del producto a devolver: "))
        valor = int(input("Ingresa el valor del producto:"))
        total_vr_p=cantidad*valor
        print("el total de",nombre_producto,"es",total_vr_p,"\n")
        suma -= total_vr_p
        print("Su total hasta el momento es:",suma)
        descuento=reinicio=input("Desea seguir eliminando el producto (S o N): ")   
        
    productos -= 1
  total += suma
  if suma > mayor:
    mayor = suma
  else:
    mayor = mayor
  
  entrada=input("Nuevo cliente (s/n): ")

if total==0:
    print("No hubo clientes en el día" )
else:
    print("Cobró total de todos los cliente: ", total )
    print("El mayor monto fue: ", mayor)

print("Gracias por utilizar este programa")