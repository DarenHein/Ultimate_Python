'''
Escribe un programa que solicite al usuario ingresar una lista de números enteros. El programa debe imprimir la suma de todos los números de la lista.


'''

lista = [1,2,3]
suma = 0 
for i in lista : 
    suma =  i + suma 
nota = open('nota2.txt','w')
suma2 = str(suma)
nota.write(suma2)
nota.close() 