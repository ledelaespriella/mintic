''' 
ejercicio de desafio:

haga un programa que permita capturar
N facturas. cada factura es calculada
de la siguiente manera:
se pide la cantidad de productos
que se va a facturar. por cada producto
y el valor unitario de cada uno de esos
productos, se calcula el subtotal por
cada  producto. 
al final se le agrega el iva y se
genera la factura con un total factura
los totales de cada factura deben ir
registrandose para posteriormente ser
procesador de la siguente manera.

1)cual fue el producto mas comprado 
  
2)mostrar todos los totales de factura
3)cual fue la factura de menor costo
4)cual fue la factura de mayor costo
5) mostrar cuales fueron las facturas
  que estuvieron por encima del promedio
  de todos las facturas y organizarlas
  en forma ascendente.
pd: desconozco el numero de facturas que 
voy a procesar. el sistema debe permitir
todas las que yo necesite sin pedir antes
cuantas facturas son.
DEBE UTILIZAR VECTORES/LISTAS Y FUNCIONES
Y/O PROCEDIMIENTOS


ej:
numero de factura:1010
cantidad de productos: 3
----------------------------
nombre del producto 1 : camisa
cantidad a llevar de camisa : 2
valor unitario: 10
subtotal-->>20
----------------------------
nombre del producto 2: pantalon
cantidad a llevar de pantalon :4
valor unitario:20
subtotal-->>80
-----------------------------
nombre del producto 3: cinturon
cantidad a llevar de cinturon :1
valor unitario:20
subtotal-->>20

TOTAL SIN IVA-->>100
TOTAL factura#1010 CON IVA--->>119
===============================
numero de factura:1020
cantidad de productos: 2
------------------------------
nombre del producto 1: SHORT
cantidad a llevar de cinturon :7
valor unitario:10
subtotal-->>70
-------------------------------
nombre del producto 2: SOMBRERO
cantidad a llevar de cinturon :1
valor unitario:10
subtotal-->>10

TOTAL SIN IVA-->>80
TOTAL factura#1020 CON IVA--->>95.2

====================================
numero de factura:1030
cantidad de productos: 1
------------------------------
nombre del producto 1: FALDA
cantidad a llevar de cinturon :3
valor unitario:50
subtotal-->>150
-------------------------------
TOTAL SIN IVA-->>150
TOTAL factura#1030 CON IVA--->>178.5
**************

INTERNAMENTE SE GENERO UN VECTOR CON
LOS TOTALES DE CADA FACTURA

facturas=[119,95.2,178.5]
promedio de facturas=130.9

por pantalla:
PRODUCTO MAS COMPRADO:SHORT con 7 productos
FACTURA DE MENOR COSTO: 95.2
FACTURA DE MAYOR COSTO:178.5
FACTURAS POR ENCIMA DEL PROMEDIO : 178.5
FACTURAS ORGANIZADAS : 
95.2
119
178.5

'''

def cantidad_productos(c_prod):
      '''Funcion para sacar las listas de cada producto'''
      productos=[] #lista para el nombre de los productos
      lista_can_prod=[] #lista para la cantidad de productos
      lista_subtotal=[] #lista para los subtotales de cada producto
      #Hago el ciclo para la n cantidad de productos que halla en la factura
      for c_1 in range(1,c_prod+1):
            print("---------------------------------")
            nombre_prod=input("Nombre del producto {}: ".format(c_1))
            productos.append(nombre_prod) #agrego el nombre del producto a la lista inicial
            can_prod=int(input("Cantidad a llevar de {}: ".format(nombre_prod)))
            lista_can_prod.append(can_prod) #agrego a la lista de la cantidad de productos
            vr_und=float(input("Valor unitario: "))
            subtotal=can_prod*vr_und 
            lista_subtotal.append(subtotal) #agrego los subtotales a la cantidad de productos
            print("Subtotal: {}".format(int(subtotal)))
      #creo una sub lista para cada factura que se vaya a ingresar
      lista_factura=[]
      lista_factura.append(productos)
      lista_factura.append(lista_can_prod)
      lista_factura.append(lista_subtotal)
      return lista_factura

def totales_fac():
      lista_factura=cantidad_productos(c_prod)
      total_factura=sum(lista_factura[2])
      iva=1.19
      total_fac_iva=total_factura*iva
      print("TOTAL SIN IVA: {}".format(total_factura))
      print("TOTAL CON IVA: {}".format(total_fac_iva))

#Entrada de datos
N=[]
N.append(int(input("Numero de Factura: "))) #Ingreso el numero de la factura
c_prod=int(input("Cantidad de productos: ")) #Ingreso la cantidad de productos por factura a procesar
#llamo la funcion para sacar la lista de cada producto
totales_fac()
r="s"
while r=="s" or r=="S":
      pass



            
      


      
