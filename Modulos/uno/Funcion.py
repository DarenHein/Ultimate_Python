'''
Contar elementos en una tupla:
Escribe un programa que solicite al usuario ingresar una serie de números separados por comas. Luego, convierte los números ingresados en una tupla y muestra la cantidad de elementos que contiene. Aquí tienes un ejemplo de cómo podría ser el código:
python

'''
def funcion() : 
    i = 0
    bandera =  True 
    tupla = ()
    lista = []
    while bandera : 
        elemento = int (input("Ingresa el elemento -> "))
        lista.insert(i,elemento)
        op = int(input("DEseas agregar otro elemnto ala tupla ? \n 1 si \n 2 no \n Digita tu opcion "))
        if op ==1 : 
            bandera = True
        elif op ==2 : 
            bandera = False
        i =  i + 1
    tupla = tuple(lista)
    print(tupla)



        


