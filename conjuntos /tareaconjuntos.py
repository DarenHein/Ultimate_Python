'''
crea dos conjuntos de frutas vegetales ropa calzado y aplica cada una de las operaciones y mas aparte que el usuario los meta 

'''
bandera = True
conjunto = {"Limon" , "Tomate" , "Tenis" , "Pantalon" , "Manzana"}
conjunto2 = {"Traje" , "Tomate" , "Zapatos" , "Short" }
conjunto3 = set()

while bandera : 
    op = int(input("""

    Lee las opciones y escoje la de tu agrado 
    1 union 
    2 interseccion 
    3 diferencia 
    4 agregar elementos 
    5 buscar elementos en el conjunto 
    6 salir 
    Digita tu opcion -> 
    """))
    if op == 1 : 
        print("Union")
        print(f'''
        Union de conjuntos 
        conjunto =  {conjunto}  
        conjunto2 = {conjunto2}
        ''')
        union = conjunto | conjunto2
        print(f'''
        La union resultante es -> {union} 
              ''')
    elif op == 2 : 
        print("Interseccion")
        print(f'''
        interceccion de los conjuntos 
        conjunto =  {conjunto}  
        conjunto2 = {conjunto2}
        ''')
        interseccion = conjunto & conjunto2
        print(f"la interccion es -> {interseccion}")
    elif op == 3 : 
        print("Diferencia")
        print(f'''
        diferencia de los conjuntos 
        conjunto =  {conjunto}  
        conjunto2 = {conjunto2}
        ''')
        diferencia = conjunto - conjunto2
        print(f"la difencia de conjuntos es -> {diferencia}")
    elif op == 4 : 
        print("Agregar elementos ")
        op = int(input("en que conjunto quieres agregar el eleemnto \n 1 - conjunto \n 2 - conjunto 2 "))
        if op == 1 : 
            palabra = input("Ingresa la fruta o articulo -> ")
            palabra2 = palabra.capitalize()
            conjunto.add(palabra2)
            print(conjunto)
        elif  op == 2 : 
            palabra = input("Ingresa la fruta o articulo -> ")
            palabra2 = palabra.capitalize()
            conjunto2.add(palabra2)
            print(conjunto2)
    elif op == 5 : 
        print("Buscar")
        palabra = input("Ingresa el nombre del articulo que deseas buscar -> ")
        palabra2 = palabra.capitalize()
        esta = palabra2 in conjunto 
        if esta == True : 
            print("El articulo se encuntra en el registro ")
        else : 
            print("El articulo no se encuentra en el registro ")
            print("ahora lo buscaremos en el siguiente conjunto ")
            esta = palabra2 in conjunto2
            if esta == True : 
                print("El articulo se encuntra en la base de datos ")
            else : 
                print("Mamaste")
        
    elif op == 6 : 
        bandera = False 
    else : 
        print("opcion invalida ")

