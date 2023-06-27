'''
hacer que el usuario cree la nota 

'''
nombre = input("ingresa el nombre de la nota .> ")
nombre = nombre + ".txt"
nota = open(nombre , 'w')
nota.write("Kevin es puto ")
nota.close()
