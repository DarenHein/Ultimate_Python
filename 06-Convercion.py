
# todo como convertir todos los tipos de datos 

edad = input("Ingresa tu edad -> ")
print(edad) # todo esto devuelve un dato de tipo string 
print(type(edad)) # todo str

# todo trasnfromar string a entero float 
edad = int(edad) # todo asi simplemente se puede trasnfromar a entero 
print(type(edad))
# float 
edad = float(edad) # todo asi se trasnforma en float osea decimaes 
print(type(edad))

# todo de numerico a string 
edad2 = int(input("ingresa tu edad -> "))
print(type(edad2))
edad2 = str(edad2)
print(type(edad2))
# todo de float a string 
edad3 = float(input("ingresa tu edad "))
print(edad)
print(type(edad))
edad = str(edad)
print(type(edad))

# todo ahora viene el dificl boooleanos 
# todo todos lo valores que queramos trasnformar a boolenos los regresara como true a exepcion de estos 
# * cero como numero 0 
# * cadena vacia " "
# *  None 
# *  False 
print(bool(None))
print(bool(""))
print(bool(0))
print(bool(True))
