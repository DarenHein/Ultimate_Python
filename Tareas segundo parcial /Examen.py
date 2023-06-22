'''
(2 puntos) Transformación de datos: #!
a) Convierte la cadena de texto "123" en un entero.#!
b) Convierte el número entero 5 en una cadena de texto.#!
(3 puntos) Listas:
a) Crea una lista llamada "numeros" con los números del 1 al 5.#!
b) Agrega el número 6 al final de la lista.#!
c) Imprime el tercer elemento de la lista.#!
(4 puntos) Diccionarios:
a) Crea un diccionario llamado "persona" con las siguientes claves y valores: "nombre" como "Juan", "edad" como 30, y "ciudad" como "Madrid".#!
b) Agrega la clave "profesión" con el valor "ingeniero" al diccionario.#!
c) Imprime el valor de la clave "edad".#!
(5 puntos) Bucles for y while:
a) Utiliza un bucle for para imprimir los números del 1 al 10.#!
b) Utiliza un bucle while para imprimir los números del 5 al 1 en orden descendente.#!
(6 puntos) Estructuras de control if-else:
a) Escribe una estructura de control if-else que verifique si un número es par o impar.#Imprime "Es par" si es par y "Es impar" si es impar. #!
b) Escribe una estructura de control if-else que verifique si un número es positivo, negativo o cero. Imprime "Positivo", "Negativo" o "Cero" según corresponda.
'''

# ! ejericio 1 
cadena = 123
numero = int(cadena)
print(numero)
print(type(numero))

# ! ejericio 2 
numero = 5 
cadena = str(numero)
print(cadena)
print(type(cadena))

#! ejericio 3 
numeros = [1,2,3,4,5,6,7,8,9,10,11]
numeros.insert(11,12)
print(numeros)
print(numeros[2])

#! ejricio 4 diccionarios 

persona = {"Nombre" : "Luis" , "Edad" : 30 , "Ciudad" : "Mexico" }
persona["Profecion"] = "Inge "
print(persona["Edad"])

#! ejericio 5 buccles for 
i = 0 
for i in range(i,101,i+1):
    print(i)

num =  int(input("Ingresa un numero "))
while num >=1 : 
    print(num) 
    num =  num -1
#! Ejercioc 6 if else 

x =  int (input("Ingresa un numero "))
if x % 2 == 0 : 
    print("El numero es par ")
elif x == 0 :
    print ("no ammes carnal no pongas cero ")
else : 
    print("El numeor no es par ")

num = int (input("Ingresa un numero "))
if num == 0 : 
    print("El numero es cero ")
elif num > 0 : 
    print("El numero es positivo ")
else : 
    print("El numero es negatvo ")