#Diccionarios
#Se basa en una estructura mapeada, donde cada elmento de la colección se encuentra identificado con una clave única. 
#No puede haber dos claves iguales, en otros lenguajes se conocen como arreglos asociativos. 

vacio = {}
print(vacio)

print(type(vacio))

#Definción,
#Para cada elemento se define una estructura, clave:valor
colores = {'amarillo': 'yellow', 'azul':'blue'}

#También se puede agregar elementos sobre la marcha: 
colores['verder'] = 'green'

print(colores)

#Obtener el valor de un elemento, se realiza a través de su clave
print(colores['azul'])

print(colores['amarillo'])

#Las claves pueden ser números, pero son un poco confusas
numeros = {1: 'uno', 2:'dos', 3:'tres'}

print(numeros[1])

#Modificación de valor a partir de la clave
colores['amarillo'] = 'white'

print(colores)

#Función del(): Sirve para borrar un elemento del diccionario. 

del(colores['amarillo'])

print(colores)

#For: Sentencia para recorrer los elementos del diccionario

edades = {'Hector':21, 'Maria':22, 'Jorge':23}

#Devuelve las claves
for edad in edades:
    print(edad)

#Para obtener los valores
for edad in edades:
    print(edades[edad])

#.items(): Métodos que nos facilita la lectura en clave y valor, porque devuelve ambos elementos en cada iteración

for c,v in edades.items():
    print(c,v)