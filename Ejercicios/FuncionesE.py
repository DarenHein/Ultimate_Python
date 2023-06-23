'''
Contar números pares e impares: Escribe una función llamada "contar_pares_impares" que tome una lista de números como argumento y cuente cuántos números son pares y cuántos son impares. La función debe imprimir el resultado. Utiliza un bucle "for" para recorrer la lista y una estructura condicional "if-else" para determinar si un número es par o impar.
'''
def numeros(lista):   
    w = 0
    z = 0
    contador_par = 0 
    contador_inpar = 0
    print("Funcion")
    i = 0 
    num = len(lista)
    while i < num : 
        aux2 = lista[i]
        aux = aux2 
        if aux % 2 == 0 : 
            print("el nuemros -< " , lista[i] , " es par")
            z = z + 1 
        else : 
            print("el nuemros -< " , lista[i] , " es inpar")
            w = w + 1 
        i = i + 1 
    print("hay -> " , z, "numeros pares ")
    print("hay -> " , w, "numeros inpares ")


print("Metodo main")
lista = []
op2 =  int(input("Ingresa los nuemeros que conforma la lista "))
i = 0 
while i < op2 : 
    num = int (input("ingresa un numero para la lista -> "))
    lista.insert(i,num)
    i = i +1 


numeros(lista)


