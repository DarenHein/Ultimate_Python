class Perro:
    def __init__(self,nombre , raza , sexo , alimento):
        self.nombre = nombre 
        self.raza = raza 
        self.sexo = sexo 
        self.alimento = alimento 
        pass
    def caracteristicas(self): 
        print("EL nombre del perro es : " , self.nombre)
        print("La raza es -> " , self.raza)
        print("El sexo del perro es -> " ,self.raza)
        print("La alimentacion es -> " , self.alimento)
    