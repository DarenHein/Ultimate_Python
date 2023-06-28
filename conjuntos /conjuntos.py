'''
los conjuntos son colecciones de datos desordenadas que no pueden tener el mismo tipo de dato dentro 
osea que si en el conjunto hya un 3 no puede hber otro 3 
'''
conjunto = {1,2,3} # conjunto con elementos 
conjunto2 = set() # conjunto vacio 

#! agregar elemntos al conjunto 
conjunto.add(5)
conjunto2.add(4)
conjunto2.add(2)
print(conjunto2)
print(conjunto)

# ? los conjuntos no tienen indices o llaves como en otras coleccios de datos por ende no se pueden mandar a llmar en solitario pero si pdodemos buscar si el elemento se encuntra en el conjunto 

print(1 in conjunto) #? devulvera un True 
print(1 in conjunto2) #? devulvera un False

#? OPERACIONES CON CONJUNTOS 
#? UNION SIMBOLO  -> |
#* la union es cuando dos conjuntos se unen y crean un conjunto con los eleemtos de ambos conjuntos si hay eleemtnos repetidos este solo aparecera una ves 
union = conjunto | conjunto2
print(union)

#? INTERSECCION 
'''
LA INTERCECCION son los elementos comunes de cada conjunto 
si el elemtno contiene 1234 y el otro solo el 2 con la interseccion solo se mostrara el 2 
su simbolo es el amperson & 
'''
interseccion = conjunto & conjunto2
print(interseccion)

#? DIFERENCIA 
'''
la diferencia de conjuntos son los elementos que no se encuentrar entre ambos conjuntos osea si al conjunto a y conjunto b solo comparten el 2 se mostraran los demas elementos de dicho conjunto no es lo mismo diferencia entre a y b que b y a 

#? su simbolo es el menos - 
'''
diferencia =  conjunto - conjunto2
print(diferencia)
