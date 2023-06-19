
# todo crear un etuipo de funtbool con biblotecas

portero = []
delanteros = []
defensas = []
centros=[]
i = 0 ; 
print("Porteros")
while i < 2 : 
    aux = input(f"{i+1} Ingresa el nombre del jugador -> ")
    portero.insert(i,aux)
    i =  i + 1
print("Delanteros")
i = 0
while i < 5 : 
    aux = input(f" {i+1} Ingresa el nomre de los delanteros -> ")
    delanteros.insert(i,aux)
    i =  i +1 
i = 0 
print("Defensas")
while i < 2 : 
    aux = input(f" {i+1} Ingresa el nomre de los defensas -> ")
    defensas.insert(i,aux)
    i = i + 1
print("Centros")
i = 0 
while i < 2 : 
    aux = input(f" {i+1} Ingresa el nomre de los Centros -> ")
    centros.insert(i,aux)
    i = i + 1

    
# todo salimos del bucle for 
print("\nMostrar datos")
equipo = {"Porteros": portero , "Delanteros" : delanteros , "Defensas" : defensas , "Centros" : centros}

for dato,valor in equipo.items() : 
    print(dato ,":" ,valor)


