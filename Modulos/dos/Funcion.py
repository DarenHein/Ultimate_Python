'''
dada una tupla de numeros crea la multiplicaionn de esa tupla 
'''
def tupla(): 
    tupla = (1,2,3,4,5)
    tupla = tupla * 3 
    print(tupla)
    nueva = tuple(x*2 for x in tupla)
    print(nueva)
def palabras() : 
    # Dada una lista de palabras, imprime las palabras que tengan una longitud mayor a 5 caracteres.
    lista = ["Luis" , "Kelly"]
    for i in lista : 
        aux =  len(i)
        print("la palbra contiene -> ",aux , " letras")
def estudiantes() : 
    # Dado un diccionario de estudiantes y sus calificaciones, obtén una lista con los estudiantes que aprobaron (calificación mayor o igual a 60).
    diccionario = {"luis" : 10 , "Kelly" : 10}
    for llave,dato in diccionario.items() : 
        if dato >= 10 : 
            print("Pasa" , llave )
        else : 
            print("no pasa " , llave)

    
