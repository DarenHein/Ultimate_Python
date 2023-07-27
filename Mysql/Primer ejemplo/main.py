import mysql.connector


# Todo: main 
#todo vamos a crear la conexion con la base de datos en el main 
nombre = "root" #! siempre es root 
contra = "58825613" #! contrseña de mysql 
host = "localhost"#! si estamos en nuestra maquina es localhost
baseD = "utc" #! nombre de la base de datos 
try : 
    conexion = mysql.connector.connect( #todo : metodo con el que conectamos la base de datos lso datos siguientes son los necesarios para la conexion con la base de datos 
    user = nombre,
    password = contra,
    host = host,
    database = baseD
    )
    print("conexion exitosa con la base de datos ")
except mysql.connector.Error as erro : 
    print("Erroe en la conexxcion de base de datos " , erro)

#todo : ahora necesitamos un objeto que nos ayude con la manipulacion de la base de datos 
cursor = conexion.cursor() #todo esta tiene el nombre de la 

print('''
1 - Materias nuevas 
2 - Ver materias 
3 - Borrar materias
4 - Salir 
''')
op = int(input("Ingresa la opción deseada: "))

if op == 1:
    #todo ahroa insertaremos elemtos ala base de datos 
    materia = input("Ingresa el nombre de la materia -> ")
    numero = input("Ingresa el numero de la materia o id -> ")
    consulta = "INSERT INTO materias (nueva, numero) VALUES (%s, %s)"
    valores = (materia, numero)
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
elif op == 2: 
    #todo ver los datos que estan dentro de la tabla 
    consulta = "SELECT * FROM materias" #! esta variable contiene una instruccion a aql 
    cursor.execute(consulta) #! cursor nos permite interactuar con sql execute sirve para mandar la instruccion almacenada en la variable consulta 
    #todo ahora mostraremos los datos en la pantalla de sql 
    resultados = cursor.fetchall() #! fetchall nos decuelve una tupla con los elementos que se encuentren dentro de la table de la base de datos 
    for fila in resultados:
        print(fila) #* lo que etsamo haciendo con el for s que la tupla devuelta recorrera fila por fila de la variebl resultado y nos devolvera resultados
    #todo importante cerrar la base de datos y el cursor 
    cursor.close()
    conexion.close()

elif op == 3: 
    consulta = "DELETE FROM materias WHERE numero = %s"
    numero_eliminar = input("Ingresa el numero (id) a eliminar ->")
    cursor.execute(consulta,(numero_eliminar,))
    conexion.commit()
    cursor.close()
    conexion.close()
elif op == 4: 
    pass
    print ("Gerson es puto")
else: 
    print("Opción inválida")
