
bandera = True

while bandera : 
        opc = int(input('''

"Escoge una opcion \n 1.unionde los conjuntos a,b,c,d \n 2.interseccionde los conjuntos a,b \n 3.interseccionde los conjuntos c,d \n 4.interseccionde los conjuntos a,b,c,d \n 5 salir "

''')) # opc = input() que mierdas no mames 
a=set(["pantalon","camisa","short","playera","calcetines"])
b={"pantalon","camisa","playera","sudadera","chamarra","corbata"}
c={"pantalon","short","calcetines","zapatos","tenis"}
d={"pantalon","camisa","short","playera","calcetines","sudadera","zapatos","chamarra","tenis","corbata"}
# unionde todos los conjuntos
if opc==1 : #! esto no es c ni java no mames no va con llaves ni parentesis 

    union_todos=a.union(b).union(c).union(d) #! pendeja hay algo que se llam indentado 
    print("unionde los conjuntos a,b,c,d: ", union_todos)

#interseccionde conjunto a y conjunto b

elif opc == 2 : 
    a_b=a.intersection(b) #! por que no ocupas los simbolos logicos no mames 
    print("interseccionde los conjuntos a,b: ",a_b)
    #interseccionde conjunto c y conjunto d
elif opc == 3 : 
    c_d=c.intersection(d)
    print("interseccionde los conjuntos c,d: ",c_d)
elif opc == 4 : 
    #interseccionde los conjuntos a,b,cy d
    inter_todos=a.intersection(b).intersection(c).intersection(d)
    print("interseccionde los conjuntos a,b,c,d: ",inter_todos)
elif opc == 5 : 
    bandera = False 

else : 
    print("Fanny no mames habeses me soprende tu pendejes ")

print(a -b)
 # elementos de a que no pertenecen b
print(b -a)
 # elementos de b que no pertenecen a
print(a ^ b)
 # los elementos interseccionno se muestran