'''
Escribe un programa que permita gestionar una lista de alumnos y sus calificaciones. El programa debe tener las siguientes funcionalidades:

Una función llamada "agregar_alumno" que tome como argumentos un diccionario para almacenar la información del alumno, incluyendo su nombre y calificación. La función debe solicitar al usuario que ingrese el nombre y la calificación del alumno, y luego agregar esos datos al diccionario.
Una función llamada "mostrar_alumnos" que tome como argumento una lista de diccionarios, donde cada diccionario representa a un alumno. La función debe mostrar por pantalla el nombre y la calificación de cada alumno en la lista.
Una función llamada "promedio_calificaciones" que tome como argumento una lista de diccionarios de alumnos y calcule el promedio de las calificaciones. La función debe devolver el promedio.

'''

def agregar() : 
    print("Agregar el alumno")
    dic = {}
    bandera =  True
    while bandera : 
        nombre = input("Ingresa el nombre del alumno -> ") 
        cali = int(input("Ingresa su calificaion -> "))
        dic[nombre] = cali 
        print ("deseas de dejar de agregar alumnos ? ")
        print("1 si <")
        print("2 no <")
        op = (int(input("Digita tu opcion -> ")))
        if op == 1 :
            bandera = True 
        elif op == 2 : 
            bandera = False

    for llave , dato in dic.items() : 
        print ( llave , dato )

print("Main")
agregar() 