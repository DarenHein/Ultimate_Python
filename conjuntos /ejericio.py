'''
Ejercicio 1: Unión de conjuntos
Dado un conjunto de números, realiza una función que reciba dos conjuntos y devuelva la unión de ambos conjuntos.

'''
def union(conjunto,conjunto2): 
    union  = conjunto | conjunto2
    return union

conjunto = {1,2,3,4,5,6}
conjunto2 = {6,7,8,9,10}
uni = union(conjunto,conjunto2)
print(uni)

    