'''
operaciones basicoas con conjuntos 
'''
def uni(conjunto,conjunto2): 
    union = conjunto | conjunto2 
    return union
def inter(conjunto,conjunto2): 
    interseccion = conjunto & conjunto2 
    return interseccion
def dife(conjunto,conjunto2): 
    diferencia = conjunto - conjunto2 
    return diferencia
def dife2(conjunto,conjunto2): 
    diferencia2 = conjunto2 -conjunto
    return diferencia2
bandera = True 
while bandera : 
    conjunto = {1,2,4,12}
    conjunto2 = {13,12,1,3,4}
    print('''

 ######   #######  ##    ##       ## ##     ## ##    ## ########  #######   ######     
##    ## ##     ## ###   ##       ## ##     ## ###   ##    ##    ##     ## ##    ##    
##       ##     ## ####  ##       ## ##     ## ####  ##    ##    ##     ## ##          
##       ##     ## ## ## ##       ## ##     ## ## ## ##    ##    ##     ##  ######     
##       ##     ## ##  #### ##    ## ##     ## ##  ####    ##    ##     ##       ##    
##    ## ##     ## ##   ### ##    ## ##     ## ##   ###    ##    ##     ## ##    ##    
 ######   #######  ##    ##  ######   #######  ##    ##    ##     #######   ######     
     
     ''')


    print ('''

Lee las opciones de operaciones con conjuntos y escoje la de tu agrado 
1 - union 
2 - interseccion 
3 - direncia 
4 - mostrar todo 
5 - salir 

''')
    op = int (input("Ingresa tu opcion -> "))
    if op ==1 : 
        print('''
##     ## ##    ## ####  #######  ##    ## 
##     ## ###   ##  ##  ##     ## ###   ## 
##     ## ####  ##  ##  ##     ## ####  ## 
##     ## ## ## ##  ##  ##     ## ## ## ## 
##     ## ##  ####  ##  ##     ## ##  #### 
##     ## ##   ###  ##  ##     ## ##   ### 
 #######  ##    ## ####  #######  ##    ## 
        ''')
        union = uni(conjunto,conjunto2)
        print(union)
    elif op == 2 : 
        print('''

#### ##    ## ######## ######## ########   ######  ########  ######   ######  #### ##    ## 
 ##  ###   ##    ##    ##       ##     ## ##    ## ##       ##    ## ##    ##  ##  ###   ## 
 ##  ####  ##    ##    ##       ##     ## ##       ##       ##       ##        ##  ####  ## 
 ##  ## ## ##    ##    ######   ########   ######  ######   ##       ##        ##  ## ## ## 
 ##  ##  ####    ##    ##       ##   ##         ## ##       ##       ##        ##  ##  #### 
 ##  ##   ###    ##    ##       ##    ##  ##    ## ##       ##    ## ##    ##  ##  ##   ### 
#### ##    ##    ##    ######## ##     ##  ######  ########  ######   ######  #### ##    ## 
        
        ''')
        inter = inter(conjunto,conjunto2)
        print(inter)
    elif op == 3 : 
        print('''
########  #### ######## ######## ########  ######## ##    ##  ######  ####    ###    
##     ##  ##  ##       ##       ##     ## ##       ###   ## ##    ##  ##    ## ##   
##     ##  ##  ##       ##       ##     ## ##       ####  ## ##        ##   ##   ##  
##     ##  ##  ######   ######   ########  ######   ## ## ## ##        ##  ##     ## 
##     ##  ##  ##       ##       ##   ##   ##       ##  #### ##        ##  ######### 
##     ##  ##  ##       ##       ##    ##  ##       ##   ### ##    ##  ##  ##     ## 
########  #### ##       ######## ##     ## ######## ##    ##  ######  #### ##     ## 
        
        ''')
        diferencia = dife(conjunto,conjunto2)
        print("Diferencia entre conjunto a y b ".diferencia)
        diferencia2 = dife2(conjunto,conjunto2)
        print("Diferencia entre el conjunto b y a ", diferencia2)
    elif op == 4 : 
        print("aqui se muestra todas las opreaciones pero de forma aburrida ")
        print(conjunto)
        print(conjunto2)
        union = uni(conjunto,conjunto2)
        inter = inter(conjunto,conjunto2)
        difer = dife(conjunto,conjunto2)
        print(f'''
            union -> {union}
            interseccion -> {inter}
            diferencia -> {difer}
            son todas las operaciones 
        ''')
    elif op == 5 : 
        bandera = False 
    else : 
        print("Opcion invalida intenta otra vez ")

