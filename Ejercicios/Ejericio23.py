# Imagina que estás creando un sistema de reservas para un cine.
# Cada película tiene un título, horarios disponibles y el número de asientos disponibles en cada horario.

# Definir la información de las películas y sus horarios
peliculas = {
    "Avengers: Endgame": [("12:00 PM", 50), ("3:00 PM", 30), ("6:00 PM", 20)],
    "El Rey Leon": [("2:00 PM", 40), ("5:00 PM", 50)],
    "La La Land": [("4:00 PM", 60)]
}

# Mostrar la lista de películas disponibles

print("La cartelera es la siguiente : ") 
for llave , dato in peliculas.items() : 
    print(llave)
    
#! Solicitar al usuario seleccionar una película
nombre_pelicula = input("Ingresa el nombre de la pelicula -> ")
#! Verificar si la película seleccionada existe en el sistema
for llave,dato in peliculas.items() : 
    if nombre_pelicula == llave : 
        print("Pelicula existe en cartelera")
        pelicula_seleccionada = llave 
        horario = dato
#! Mostrar los horarios disponibles para la película seleccionada
print("pelicula -> " , pelicula_seleccionada , "horarios -> " , horario)
# Verificar si hay asientos disponibles
print(peliculas.get(pelicula_seleccionada))

