class Gato:
    def __init__(self,nombre , raza , sexo , alimentacion):
        self.nombre = nombre 
        self.raza = raza 
        self.sexo = sexo 
        self.alimentacion = alimentacion
        pass
    def caracteristicas(self): 
        print("nombre : ",self.nombre)
        print("raza : ",self.raza)
        print("sexo : " , self.sexo)
        print("alimento" , self.alimentacion)
        
