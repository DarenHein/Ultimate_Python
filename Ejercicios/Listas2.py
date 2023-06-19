

personas = []
i = 0

while True : 
    print("\n \n")
    print("Porgrama que almacena elimina y muestra listas de personas ")
    print ("Lee las opciones y escoje la de tu agrado ")
    print ("1 agregar persona ")
    print ("2 eliminar persona ")
    print ("3 eliminar toda la lista ")
    print("4 personas registradas ")
    op = int(input("ingresa tu opcion -> "))
    if op == 1 : 
        print("\n \n")
        print("agregar personas ")
        nombre = input("Agrega el nombre -> ")
        personas.insert(i , nombre)
        i = i + 1 
    elif op == 2 : 
        print("\n \n")
        print("Eliminar personas ")
        print("Las personas regristradas son las siguientes : ")
        print(personas)
        nombre = input("ingresa el nombre de la eprsona que deseas eliminar ")
        personas.remove(nombre)
        print("personas eliminadas ")
        print(personas)
    elif op ==3 : 
        print("\n \n")
        print("Eliminar toda la lista")
        personas.clear()
        print("personas eliminadas con exito")
    elif op == 4 : 
        print("\n \n")
        print("Mostrar  personas ")
        print(personas)