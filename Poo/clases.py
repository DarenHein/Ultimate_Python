class Perro: #! creacion de la clase 
    def __init__(self, nombre, edad): #! una funcion con paramtros nombre edad 
        #! self es no se pasa parametro es como llamarse a si misma 
        #? esto seria como el constructor en java 
        self.nombre = nombre #! atributos seria como el this.nombre = nombre en java 
        self.edad = edad

    def ladrar(self): #! metodo lleva el self como parametro 
        print(f"{self.nombre} está ladrando ¡Guau, guau!")

    def correr(self):#! metodo lleva el self como paramtro para llamarse asi misma 
        print(f"{self.nombre} está corriendo a toda velocidad!")

# Crear objetos de la clase Perro
perro1 = Perro("Max", 3)
perro2 = Perro("Bella", 5)

# Acceder a los atributos y métodos de los objetos
print(perro1.nombre)  # Imprime "Max"
print(perro2.edad)    # Imprime 5

perro1.ladrar()       # Imprime "Max está ladrando ¡Guau, guau!"
perro2.correr()       # Imprime "Bella está corriendo a toda velocidad!"
