#Textos (cadenas de caracteres)
print("Hola mundo")
print('Hola mundo')
print("Este texto incluye unas '' ")
print('Este texto incluye unas "" ')
print("Esta 'palabra' se encuentra escrita entre comillas simples")
print('Esta "palabra" se encuentra escrita entre comillas dobles ')
print("Esta \"palabra\" se encuentra escrita entre comillas dobles")
print('Esta \'palabra\' se encuentra escrita entre comillas simples')
print("Un texto \tuna tabulacion")
print("Un texto \nuna nueva linea ")

c = "Cadena en variable"
print(c)

#Operaciones
c2 = "Cadena 2"
print(c+c2)
s = "Una cadena " "compuesta de dos cadenas"
print(s)

#Se puede multiplicar cadenas
diez_espacios = " " * 10
print(diez_espacios + " un texto luego de 10 espacios")

#Indices
palabra = "Python"
print(palabra[0])

#El indice negativo -1, hace referencia al carácter de la última posición, el -2 al penúltimo y asi sucesivamente
print(palabra[-1])
print(palabra[-2])

#Slicing - Substring o Subcadenas
print(palabra[0:2])
print(palabra[2:])
print(palabra[:2])

#De principio a fin
print(palabra[:])

#Las cadenas son inmutables, es decir, no se pueden modificar
#Esto da error: 
#palabra[0] = "N"

#Funciones, len() permite saber la longitud de una cadena
print(len('Esto es una cadena'))


