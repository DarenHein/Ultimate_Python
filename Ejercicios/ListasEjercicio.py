'''
Ejercicio 2: Listas
Crea una lista llamada "frutas" que contenga cinco frutas diferentes. Realiza las siguientes acciones:

Imprime la fruta en la segunda posición de la lista.
Agrega dos frutas más a la lista.
Ordena la lista alfabéticamente.
Elimina la fruta en la cuarta posición de la lista.
Imprime el número total de frutas en la lista.
'''
# ejercicio 1 
frutas = ["Manzana" , "Naranja " , "Limon "]
print(frutas[1])

#ejerciio 2
frutas.insert(1,"Durazno")
frutas.insert(2,"Tomate")
print(frutas)

# ejercicio 3 
# este si no amme 

#ejericio 4 
frutas.remove("Manzana")
print(frutas)

#ejericio 5 este no lo entiendo si quiere que muestre toda la lista o que solo cuantos elemntos hay 

numero = len(frutas)
print(numero)
print(frutas)