'''
¡Claro! Aquí tienes algunos ejercicios con bucles `for` en Python para que puedas resolverlos sin las respuestas proporcionadas. ¡Diviértete resolviéndolos!

1. Ejercicio de suma de elementos:
   Escribe un programa que calcule la suma de todos los elementos en una lista dada. Utiliza un bucle `for` para recorrer la lista y acumular la suma.

2. Ejercicio de conteo de vocales:
   Escribe un programa que cuente la cantidad de vocales en una cadena de texto dada. Utiliza un bucle `for` para recorrer cada carácter de la cadena y verifica si es una vocal.

3. Ejercicio de búsqueda de elemento:
   Escribe un programa que busque la posición de un elemento específico en una lista dada. Utiliza un bucle `for` para recorrer la lista y compara cada elemento con el valor buscado.

4. Ejercicio de multiplicación de elementos:
   Escribe un programa que multiplique todos los elementos en una lista dada por un número escalar. Utiliza un bucle `for` para recorrer la lista y multiplica cada elemento por el número escalar.

5. Ejercicio de impresión de patrón:
   Escribe un programa que imprima un patrón triangular utilizando un bucle `for`. El patrón debe tener un número creciente de asteriscos en cada línea.

Recuerda que estos ejercicios están diseñados para practicar el uso de bucles `for` en Python. Intenta resolverlos por tu cuenta y si tienes alguna pregunta o necesitas ayuda, estaré aquí para asistirte. ¡Buena suerte!

'''

lista = [1,2,3,4,5,6]
suma = 0 ; 
for i in lista : 
    suma =  suma + i

print("La suma total de los numeros -> " , suma )

palabra = "Hola"
conteo = len(palabra)
for i in palabra :
    print(i) 
print("la palabra cuneta con -> " , conteo )

lista2 = ["zapato" , "chettos" , "flor " , "refresco"]
palabra = input("Ingresa una palabra y busquemos si se encunetra en la lista -> ")
for i in lista2 : 
    if palabra == i : 
        print("palabra encontrada ")

lista3 =[1,2,3,4]
lista4 =[]
escalar = 3 
contador = 0

for i in lista3 : 
    i = i * escalar
    lista4.insert(contador,i)

print("La multiplicaicion de la lista por un escalar es de -> " ,lista4)

numero = int(input("Ingrese un número entero positivo: "))

for i in range(1, numero + 1):
    linea = "*" * i
    print(linea)


    