#Conjuntos: 
#Son colecciones desordenadas de elementos únicos utilizados para hacer pruebas de pertenencia de grupos y eliminación de elementos duplicados

conjuntos = set()

conjunto = {1,2,3}

print(conjunto)

#Métodos add(): Sirve para añadir elementos al conjunto. Si un elemento ya se encuentra no se añadirá de nuevo. 
conjunto.add(4)
print(conjunto)

conjunto.add(0)

print(conjunto)

conjunto.add(4)

print(conjunto)

#Son colecciones desordenadas porque gestionan automáticamente la posición de sus elementos, en lugar de conservar la posición en que fueron añadidos
conjunto.add("H")

conjunto.add("A")

conjunto.add("Z")

print(conjunto)

#Pertenencia de grupos con "in" 

grupo = {'Hector', 'Juan', 'Mario'}

print('Hector' in grupo)
print('Luis' in grupo)

#Autoeliminación de elementos duplicados
test = {'Hector', 'Hector', 'Hector'}
print(test)

#Cast de Lista a Conjunto y viceversa

l = [1, 2, 3, 3, 2, 1]
print(l)

c = set(l)

print(c)

l = list(c)

print(l)

#Cast de Cadena a Conjunto
#Sirve para crear un conjunto con todos los caracteres de una cadena

s = "Al pan pan y al vino vino"

c = set(s)

print(c)







