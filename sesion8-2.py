"""
Ejercicio1:
haga una aplicacion en python que dado un curso de N
estudiantes en donde cada estudiantes tiene N materias
y en cada materia tiene N notas.
desplegar por pantalla cual es la Mayor nota por materia
y cual sera la mayor nota por estudiantes.
"""

estudiante=int(input("Ingrese la cantidad de estudiantes: "))
c_1=1
nota_mayor_estudiante=0
#establezco la condicion para analizar las materias que hay por cada estudiante que haya
while c_1<=estudiante:
    materias=int(input("Ingrese la cantidad de materias del estudiante "+str(c_1)+":"))
    c_2=1
    nota_mayor_materia=0
    #establezco la condicion para analizar las notas por cada materia
    while c_2<=materias:
        nombre_materia=input("Ingrese el nombre de la materia "+str(c_2)+":")
        cantidad_notas=float(input("Ingrese la cantidad de notas que se tomaron en "+str(nombre_materia)+" del estudiante "+str(c_1)+":"))
        c_3=1
        nota_mayor=0
        #estableco la condicion para calcular la mayor nota de esta materia
        while c_3<=cantidad_notas:
            nota=float(input("Ingrese la nota de la materia de "+str(nombre_materia)+" por favor: "))
            if nota>=nota_mayor:
                nota_mayor=nota
            c_3+=1 #contador de las notas
        print("La mayor nota de ",nombre_materia," fue: ",nota_mayor)
        #desarrollo una condicicion para guardar la mayor de las notas de la materia
        if nota_mayor>=nota_mayor_materia:
            nota_mayor_materia=nota_mayor
        c_2+=1 ##contador de las materias
    print("La mayor nota de todas las materias del estudiante "+str(c_1)+" fue: ",nota_mayor_materia)
    #desarrollo una condicion para guardar la mayor de las notas de los estudiantes
    if nota_mayor_materia>=nota_mayor_estudiante:
        nota_mayor_estudiante=nota_mayor_materia
    c_1+=1 #contador de los estudiantes
print("La mayor nota de los "+str(c_1)+" estudiantes ingresados al sistema fue: ",nota_mayor_estudiante)