#Iteraciones: Iterar significa realizar una acción varias veces, cada vez que se repite se denomina iteración. 
#Sentencia While: 
#Se basa en repetir un bloque a partir de evaluar una condición lógica, siempre que esta sea True. 

c = 0
while(c <= 5):
    c += 1
    print("c vale", c)

#Sentencia Else en buclhe while
c = 0
while(c <= 5):
    c += 1
    print("c vale", c)
else:
    print("se completo la intereacion c vale", c)

#Instruccción break: 
#Sirve para romper la ejecución del while, no se ejecutará el else, ya que este sólo se llama al finalizar la iteración 

c = 0 
while(c <= 5):
    c += 1 
    if(4 == c):
        print("c vale ", c, "rompemos la iteracion")
        break
    print("c vale", c)
else:
    print("Se ha completado la iteracion c vale", c)

#Instrucción continue
#Sirve para saltarse la iteración sin romper el bucle

c = 0
while (c <= 5):
    c += 1
    if(c == 3 or c == 4):
        continue
    print("c vale", c)
else:
    print("Termino la iteracion y c vale", c)

