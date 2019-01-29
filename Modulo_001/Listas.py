numeros = [1,2,3,4,5]
datos = [1,2,"tres", 3.4, "otra cadena"]

#Indices y Slicing: Funcionan muy similar a las cadenas de caracteres
print(datos[0])
print(datos[:2])

#Suma de listas

print(numeros + [6, 7, 8, 9])

#Son midificables
pares = [1,4,6,8,10]
pares[0] = 2
print(pares)

#Funciones
#.append(), para añadir un item al final de la lista
pares.append(12)
print(pares)

#len() la longitud de la lista
print(len(pares))

