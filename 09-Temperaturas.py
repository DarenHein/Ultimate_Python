
#! convertirodr de temperaturas en python 

print("Lee las opcionees y escoje la de tu agrado ")
print(" 'c' celcius a Farenheit ")
print(" 'f' farenheit a celcius")
op = input("Ingresa tu opcion -> ")
if op == 'c' : 
    print("Celcius")
    c = float(input("ingresa los grados celcius -> "))
    f = (c * 1.8) + 32
    print(f"los grados \ncelcius -> {c} \nfarenheit -> {f}")
elif op == 'f' : 
    print("Farenheit")
    f = float(input("Ingresa los grados Farenheit -> "))
    c = (f * 32) / 18
    print(f"los grados \ncelcius -> {c} \nfarenheit -> {f}")
else : 
    print("Opcion invalida")