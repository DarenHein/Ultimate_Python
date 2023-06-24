'''
las tuplas como las listas y diccionarios son colecciones de datos estas colecciones a diferencia de las listas y diccionarios 

#todo es que no se pueden modificar unas ves declaradas 

las tuplas se ocupan con () ahora vremos un ejemplo de tupls 

'''
mi_tupla = (1,2,3,4,5) #! crear tupla 
print(mi_tupla) #! imprimir tupla completa 

#? imprimir elemntos de la tupla en especifico 

print(mi_tupla[0])
print(mi_tupla[1])
print(mi_tupla[2])
print(mi_tupla[3])
print(mi_tupla[4])

#? saber cuantos elementos tiene la tupla 

numeros = len(mi_tupla)
print(numeros)

#? multiplicar tupla 
multi = mi_tupla * 2 #todo esto duplicara los elemtos d ela tupla 
print(multi)

#? trasnformar lista en tupla 
lista = [1,2,3,4]
mi_tupla2 = tuple(lista)

print(mi_tupla2)