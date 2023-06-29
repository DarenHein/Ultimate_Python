'''
Crea una clase llamada Rectangulo que tenga un constructor para inicializar el ancho y el alto del rectángulo. Luego, agrega un método llamado calcular_area que devuelva el área del rectángulo.
'''
class rectangulo : 
    def __init__(self,altura,base): 
        self.altura = altura
        self.base = base
    def calcular_area(self):
        resultado = base * altura 
        print("El area es -> " , resultado)

altura = float(input("Ingresa la altura -> "))
base = float(input("Ingresa la base -> "))   
obj = rectangulo(altura,base)
obj.calcular_area()
