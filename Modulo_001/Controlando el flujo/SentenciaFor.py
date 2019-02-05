#For (Para) con listas
numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    print(numero)

#Modificando los valores de una lista
indice = 0
for numero in numeros:
    numeros[indice] *= 10
    indice += 1
print(numeros)

#Con la funcion enumerate() podemos obtener el indice de cada valor facilmente: 
for indice, numero in enumerate(numeros):
    numeros[indice] *= 10
print(numeros)

#For en cadenas
cadena = "Hola, como estas?"
for caracter in cadena:
    print(caracter)

#Función range(): sirve para generar una lista de numeros que podemos recorrer fácilmente 
for i in range(10):
    print("i vale, ",i, "con el range")

for i in [1,2,3,4,5,6,7,8,9]:
    print(i)

#Partiendo de un range() podemos obtener la lista: 
print(list(range(10)))