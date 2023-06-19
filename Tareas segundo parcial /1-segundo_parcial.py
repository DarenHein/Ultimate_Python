
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

# todo ahora viene lo mio 
print("\n")
while True : 
    menu = """
    1 modificar 
    2 eliminar bibloteca completa alv 
    """
    print ("Lee las opciones y escoje la de tu agrado : ")
    print(menu)
    op = int(input("Digita tu opcion -> "))
    if op == 1 : 
        # todo se elimina todo alv 
        equipo.clear()
        for dato,valor in equipo.items() : 
            print(dato , ":" , valor)

