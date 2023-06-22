'''
Ejercicio 3: Combinación de diccionarios y listas
Crea un diccionario llamado "inventario" que contenga información sobre los productos en una tienda. Cada clave del diccionario será el nombre de un producto y su valor será una lista que contiene el precio y la cantidad disponible. Realiza las siguientes acciones:

Agrega tres productos al diccionario "inventario" con sus respectivos precios y cantidades disponibles.
Imprime el precio del segundo producto.
Actualiza la cantidad disponible del primer producto.
Imprime todos los productos en el inventario, junto con su precio y cantidad disponible.

'''
inventario = {"Coca" : 12 , "Pepsi" : 12 }

# agrega 3 elemntos nuevos 
inventario["Fanta"] = 12 
inventario["Seven"] = 12 
inventario["agua"] = 12 

print(inventario["Pepsi"])


inventario["Coca"] = 20 

for llave , dato in inventario.items() : 
    print(llave,dato)
