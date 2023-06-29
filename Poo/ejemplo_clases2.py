'''
una clase es como un molde donde se crean multiples objetos 
'''
class Perro: 
    def __init__(self,nombre,edad): #! constructor 
        self.nombre= nombre 
        self.edad=edad
    def ladrar(self) : #! metodo que ocuapa los atributos 
        print(f"el perro {nombre} tiene {edad}") 


nombre = input("Ingresa el nombre del perrito -> ") #! pedimos los datos 
edad = int(input("ingresa la edad del perro -> ")) #! datos 
perro1 = Perro(nombre,edad) #! creamos el objeto o instanciamos y manda
print(f"el can se llama {perro1.nombre} y tiene {perro1.edad}")
perro1.ladrar()#! mandamos a llamr al metodo 
