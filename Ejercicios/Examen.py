''' 
Parte Práctica:

Escribe un bucle for que itere sobre una lista de números del 1 al 10 e imprima cada número multiplicado por 2.

Escribe un bucle while que imprima los números del 1 al 5 y luego detenga la ejecución.

Dada una lista de strings frutas = ["manzana", "banana", "naranja", "kiwi"], utiliza un método de transformación de datos para convertir todas las frutas a letras mayúsculas y almacenar el resultado en una nueva lista llamada frutas_mayusculas. Luego, imprime el contenido de frutas_mayusculas.

Dada una lista de números numeros = [10, 20, 30, 40, 50], utiliza un método de transformación de datos para calcular el cuadrado de cada número y almacenar el resultado en una nueva lista llamada cuadrados. Luego, imprime el contenido de cuadrados.

'''

lista = [1,2,3,4,5,6,7,8,9,10] 

print("Ejercicio 1")
for i in lista : 
    print(i)

print("\n") 

print("Ejericio 2 ")
i = 0 
while i <= 10 : 
    print(i)
    i = i+1 
print("\n")
print("ejercicio 3 ")
frutas = ["manzana", "banana", "naranja", "kiwi"]
mayusculas = []
minusculas = []
print("Mayuscula")
i = 0 
while i < len(frutas) : 
    aux = frutas[i]
    aux = aux.upper(); 
    mayusculas.insert(i,aux)
    i =  i + 1 

print(mayusculas)

print("minusculas")
i = 0 
while i < len(frutas) : 
    aux = frutas[i]
    aux = aux.lower()
    minusculas.insert(i,aux)
    i =  i + 1
print(minusculas)

print("\n")
print("Ejercicio 4 ")
numeros =  [10,20,30,40,50]
numerosC = []
i = 0
while i < len(numeros) : 
    aux = numeros[i]
    aux = aux*aux
    numerosC.insert(i,aux)
    i = i + 1
print(numerosC)

