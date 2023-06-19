'''
Diccionarios 

los diccionarios son colecciones de datos como las listas y tuplas 
a diferecnia de estos que son como arregloes que tienen un indice numerico lso diccioanrios tienen una clave para acceder a ellos la clave es un numero int o palabra String 

hay que verlos como un diccionario en la vida real que tiene una palabra y esta palabra le sigue una descripcion 

'''

diccionario = {"Luis" : 30 , "Kelly" : 30 } # todo el primer parametro entre comillas es la llave despues de los dos puntos es el dato 

#todo imprimir a un dato del diccionario 
print(diccionario["Luis"]) # todo imprimira 30 que es el dato 
aux = diccionario["Luis"] # todo almacenar el valor de la llave en una variable 
print(aux)

# todo modificar el valor de un diccioaraio 
diccionario["Luis"] = 31
print(diccionario["Luis"])

#todo agregar un valor y una llave nueva al diccioanrop 
diccionario["Adobo"] = 22

# todo mostrar todo el diccionarop completo 

for clave,valor in diccionario.items(): 
    print(clave , ":" , valor)