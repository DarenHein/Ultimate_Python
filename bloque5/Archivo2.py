'''
escribir en la nota y despies leerla 

'''
nota = open('hola2.txt','w')
nota.write("\n\n el luis es un put ")
nota.close() 
nota = open('hola2.txt','r')
leer = nota.read()
print(leer)
nota.close()

'''
hay algo que aun no me queda claro al escribir en una nota esta sobreescribe y elimina el etxto existente eso no me agrada ya que si quiero haer una base de datos local no puedo llevar un conteo 
'''