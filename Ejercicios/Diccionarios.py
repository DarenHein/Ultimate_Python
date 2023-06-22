'''
Ejercicio 1: Diccionarios
Crea un diccionario llamado "contactos" que almacene los nombres y números de teléfono de tus amigos. Realiza las siguientes acciones:

Agrega tres contactos a tu diccionario.
Imprime el número de teléfono del segundo contacto.
Elimina el primer contacto de tu diccionario.
Actualiza el número de teléfono del tercer contacto.
Imprime todos los contactos restantes en el diccionario.

'''
contactos = {"Luis" : 123, "Kelly" : 12345 , "Adobo" : 7889}

#Agrega tres contactos a tu diccionario.
contactos["Adolfo"] = 1234
for clave,valor in contactos.items() : 
    print(clave,valor)

#imprime el segundo dato 

segundo = contactos["Kelly"] # todo mostrar llav y dato 
print(segundo)

#elimina el primer contacto 

contactos.pop("Luis",[123]) #Todo eliminar llave y dato de un diccionario 

for llave,valor in contactos.items():
    print(llave,valor)

#Actualiza el nuemro de cualquier elemnto 
contactos["Kelly"] = 588265612

for llave,dato in contactos.items() : 
    print(llave,dato)



