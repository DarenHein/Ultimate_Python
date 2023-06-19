# Ejercicio: Operaciones con listas

# 1. Crea una lista llamada "numeros" con los números del 1 al 5.

numeros = [1,2,3,4,5]


# 2. Imprime la lista completa.

print(numeros)


# 3. Agrega el número 6 al final de la lista.

numeros.insert(5,6)


# 4. Imprime la lista actualizada.

print( numeros)


# 5. Inserta el número 0 al inicio de la lista.

numeros.insert(0,0)

# 6. Imprime la lista actualizada.

print(numeros)


# 7. Elimina el número 3 de la lista.

numeros.remove(3)


# 8. Imprime la lista actualizada.

print(numeros)


# 9. Ordena la lista de forma ascendente.

numeros.sort(); 


# 10. Imprime la lista ordenada.

print(numeros)


# 11. Invierte el orden de la lista.


# 12. Imprime la lista invertida.

numeros.sort(reverse=True)


# 13. Obtén la longitud de la lista.

print(numeros)

print(len(numeros))

# 14. Accede al elemento en la posición 2 de la lista y asígnalo a una variable llamada "elemento".

elemento = numeros[2]


# 15. Suma todos los elementos de la lista y asigna el resultado a una variable llamada "suma".

#Todo esto lo hize asi por que no lo pide con bucle 
suma = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4] + numeros[5]
print(f"la suma de los elemntos es -> {suma}")

