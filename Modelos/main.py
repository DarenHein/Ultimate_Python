from  modelos.perro import  Perro
from  modelos.gato import Gato

'''
como crear hererncia en mmultiples archivos 
esto sirve para comunicarion entre diferentes archivos en este ejricio lo primero que necistanmos son clases una perro y una gato que estaran en coumentos diferentes 
meterlos en una carpeta aparte 
pero importante meterla con documeno de python llamado __init__.py por que si no corre 
'''

obj = Perro("Kevin","Callejero","Indesiso","Lo que sea")
obj2 = Gato("Felipe","Bobay","MAsculino","Croquetas")
obj.caracteristicas()
obj2.caracteristicas()
