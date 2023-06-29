class perro: 
    #! contructor es el que inicializa las variables en python 
    def __init__ (self, nombre, edad): #!atributos 
        self.nombre = nombre 
        self.edad = edad 

perro1 = perro("Luis",30) #! pase de parametros o atributos 
print(perro1.nombre) #! imprime luis 
print(perro1.edad) #!imprime 30 

