'''
ahora crearemos y leeremos archivos en python 

'''
archivo = open('hola.txt', 'r') # todo abrimos el archivo y se lo asiganmos a un variable 
contenido = archivo.read() # todo el metodo read leer dice que lo que esta almacenado en archivo se leera y se almacenara en la variable contenido 
print(contenido) # todo mostrar nota 

'''
los metodos para leer son los giguientes 
uedes leer el contenido del archivo utilizando diferentes métodos:
read(): Lee todo el contenido del archivo como una cadena.
readline(): Lee una línea del archivo.
readlines(): Lee todas las líneas del archivo y las devuelve como una lista.
'''

#! SUPER IMPORTANTE CERRAR LA NOTA 
archivo.close()