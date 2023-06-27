'''
frutas para gerson 

'''
import os

        

def limpiar_pantalla():
    if os.name == 'nt':  
        os.system('cls') 
    else:
        os.system('clear') 

def caja():
    total = fruta + verduras + calzado + ropa 
    iva = total * porcentaje_iva / 100
    total = total + iva  
    print(f'''
        TICKET GRACIAS POR TU COMPRA :D 
       -------------------------------------------------------------------  
              Product      |              VENTA                 
                           | Venta por producto           Precio                                                      
           Frutas ->       | ${fruta}                   -> ${carro["Manzana"]}       
           Verduras ->     | ${verduras}                    -> ${carro["Limon"]}                
           Calzado ->      | ${calzado}                    -> ${carro["Zapatos"]}    
           Ropa   ->       | ${ropa}                    -> ${carro["Pantalon"]}  
           iva ->          | %{porcentaje_iva}
           TOTAL  ->       | ${total} mas iva                           
       --------------------------------------------------------------------
                              
    ''')
    if total >= 15000 : 
        print("Descuento del %30 ")
        print("Desea realizar la compra : ")
        print("1 si ")
        print("2 no ")
        op = int(input("Digita tu opcion -> "))
        if op == 1 : 
            print("GRACIAS POR SU COMPRA ")
            nota = open('nota.txt' , 'w')
            nota.write(f'''
             TICKET GRACIAS POR TU COMPRA :D 
       -------------------------------------------------------------------  
              Product      |              VENTA                 
                           | Venta por producto           Precio                                                      
           Frutas ->       | ${fruta}                   -> ${carro["Manzana"]}       
           Verduras ->     | ${verduras}                    -> ${carro["Limon"]}                
           Calzado ->      | ${calzado}                    -> ${carro["Zapatos"]}    
           Ropa   ->       | ${ropa}                    -> ${carro["Pantalon"]}  
           iva ->          | %{porcentaje_iva}
           TOTAL  ->       | ${total} mas iva                           
       --------------------------------------------------------------------
            ''')
            nota.close()
        else : 
            bandera = False
    elif total >= 10000 : 
        print("descuento del %20")
        print("Desea realizar la compra : ")
        print("1 si ")
        print("2 no ")
        op = int(input("Digita tu opcion -> "))
        if op == 1 : 
            print("GRACIAS POR SU COMPRA ")
            nota = open('nota.txt' , 'w')
            nota.write(f'''
             TICKET GRACIAS POR TU COMPRA :D 
       -------------------------------------------------------------------  
              Product      |              VENTA                 
                           | Venta por producto           Precio                                                      
           Frutas ->       | ${fruta}                   -> ${carro["Manzana"]}       
           Verduras ->     | ${verduras}                    -> ${carro["Limon"]}                
           Calzado ->      | ${calzado}                    -> ${carro["Zapatos"]}    
           Ropa   ->       | ${ropa}                    -> ${carro["Pantalon"]}  
           iva ->          | %{porcentaje_iva}
           TOTAL  ->       | ${total} mas iva                           
       --------------------------------------------------------------------
            ''')
            nota.close()
           
        else : 
            print("siga viendp")
        
    elif total >= 5000 : 
        print("desuento del %10 ")
        print("Desea realizar la compra : ")
        print("1 si ")
        print("2 no ")
        op = int(input("Digita tu opcion -> "))
        if op == 1 : 
            print("GRACIAS POR SU COMPRA ")
            nota = open('nota.txt' , 'w')
            nota.write(f'''
             TICKET GRACIAS POR TU COMPRA :D 
       -------------------------------------------------------------------  
              Product      |              VENTA                 
                           | Venta por producto           Precio                                                      
           Frutas ->       | ${fruta}                   -> ${carro["Manzana"]}       
           Verduras ->     | ${verduras}                    -> ${carro["Limon"]}                
           Calzado ->      | ${calzado}                    -> ${carro["Zapatos"]}    
           Ropa   ->       | ${ropa}                    -> ${carro["Pantalon"]}  
           iva ->          | %{porcentaje_iva}
           TOTAL  ->       | ${total} mas iva                           
       --------------------------------------------------------------------
            ''')
            nota.close()
            
        else : 
            print("siga viendo")
            
            
    else : 
        print("Eres probre no mereces descuento ")
        print("Desea realizar la compra : ")
        print("1 si ")
        print("2 no ")
        op = int(input("Digita tu opcion -> "))
        if op == 1 : 
            print("GRACIAS POR SU COMPRA ")
            nota = open('nota.txt' , 'w')
            nota.write(f'''
             TICKET GRACIAS POR TU COMPRA :D 
       -------------------------------------------------------------------  
              Product      |              VENTA                 
                           | Venta por producto           Precio                                                      
           Frutas ->       | ${fruta}                   -> ${carro["Manzana"]}       
           Verduras ->     | ${verduras}                    -> ${carro["Limon"]}                
           Calzado ->      | ${calzado}                    -> ${carro["Zapatos"]}    
           Ropa   ->       | ${ropa}                    -> ${carro["Pantalon"]}  
           iva ->          | %{porcentaje_iva}
           TOTAL  ->       | ${total} mas iva                           
       --------------------------------------------------------------------
            ''')
            nota.close()
            
        else : 
            print("siga viendo ")
            
    


preciofrutas = 12 
precioverduras = 15
preciocalzado = 200
precioropa = 120 
bandera = True
fruta = 0 
verduras = 0 
calzado = 0 
ropa = 0
porcentaje_iva = 16
total = 0

carro = {"Manzana" : preciofrutas , "Limon" : precioverduras , "Zapatos" : preciocalzado , "Pantalon" : precioropa}
while bandera : 
    limpiar_pantalla()
    
    print("""

    /  |/  /  (_)  ___   (_)  ___ __ __   ___  ___   ____
 / /|_/ /  / /  / _ \ / /  (_-</ // /  / _ \/ -_) / __/
/_/  /_/  /_/  /_//_//_/  /___/\_,_/  / .__/\__/ /_/   
                                     /_/ 
    
    """)
    print("Hola bienvenido al carrito de super mercado :D ")
    op = int(input("""

    Lee las opciones y escoje la de tu agrado 
    1 -> frutas 
    2 -> verduras
    3 -> calzado
    4 -> ropa 
    5 -> pagar  
    6 -> salir
    Digita tu opcion -> 
    """))
    if op == 1 : 
        limpiar_pantalla()
        print('''
          ____              __            
  / __/  ____ __ __ / /_ ___ _  ___
 / _/   / __// // // __// _ `/ (_-<
/_/    /_/   \_,_/ \__/ \_,_/ /___/
                                   
        ''')
        print("Frutas")
        print(f"Precio -> {carro['Manzana']}")
        fruta = int (input(("Ingresa la cantidad de manzanas que deseas llevar ->  ")))
        fruta = preciofrutas * fruta
        print("Compra agregada al carrito :D en el menu principal puedes checar tu carrito ")
        caja()
    elif op == 2 : 
        limpiar_pantalla()
        print('''

  _   __                __                       
 | | / / ___   ____ ___/ / __ __  ____ ___ _  ___
 | |/ / / -_) / __// _  / / // / / __// _ `/ (_-<
 |___/  \__/ /_/   \_,_/  \_,_/ /_/   \_,_/ /___/
                                                 
        
        ''')
        print("verduras")
        print(f"Precio -> {carro['Limon']}")
        verduras = int (input(("Ingresa la cantidad de los limones que deseas llevar ->  ")))
        verduras = precioverduras * verduras
        print("Compra agregada al carrito :D en el menu principal puedes checar tu carrito ")
        caja()
    elif op == 3 : 
        limpiar_pantalla()
        print('''

                         __           
 ___ ___ _   ___  ___ _ / /_ ___   ___
/_ // _ `/  / _ \/ _ `// __// _ \ (_-<
/__/\_,_/  / .__/\_,_/ \__/ \___//___/
          /_/              
        
        ''')
        print("Calzado")
        print(f"Precio -> {carro['Zapatos']}")
        calzado = int (input(("Ingresa la cantidad de zapatos que deseas llevar ->  ")))
        calzado = preciocalzado * calzado
        print("Compra agregada al carrito :D en el menu principal puedes checar tu carrito ")
        caja()

    elif op == 4 : 
        limpiar_pantalla()
        print('''

  ____ ___    ___  ___ _
 / __// _ \  / _ \/ _ `/
/_/   \___/ / .__/\_,_/ 
           /_/          
        
        ''')
        print("Ropa")
        print(f"Precio -> {carro['Pantalon']}")
        ropa = int (input(("Ingresa la cantidad de pantalones que deseas llevar ->  ")))
        ropa = precioropa * ropa
        print("Compra agregada al carrito :D en el menu principal puedes checar tu carrito ")
        caja()




    elif op == 5 : 
        limpiar_pantalla()
        print('''
  _____            _       
 / ___/ ___ _     (_) ___ _
/ /__  / _ `/    / / / _ `/
\___/  \_,_/  __/ /  \_,_/ 
             |___/ 
        
        ''')
        caja()
    elif op == 6 : 
        bandera = False

        

        
        
        


        

        

