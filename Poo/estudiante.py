'''
Ejercicio 3: Clase Estudiante
Crea una clase llamada Estudiante que tenga un constructor para inicializar el nombre y la edad del estudiante. Luego, agrega un método llamado presentarse que imprima "Hola, me llamo [nombre] y tengo [edad] años."

'''
class Estudiante: 
    def __init__(self,nombre,edad): 
        self.nombre = nombre 
        self.edad= edad
    def saludo(self): 
        print(f"hola mi nombre es {nombre} y mi edad es {edad}")
nombre = input("Ingresa tu nombre ")
nombre = nombre.capitalize()
edad = int(input("Ingresa tu edad "))
obj = Estudiante(nombre,edad)
obj.saludo()