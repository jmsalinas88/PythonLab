"""Metodos de las cadenas """

#upper(): Devuelve la cadena  con todos los caracteres en mayuscula. 

print("Hola mundo".upper())

#lower(): Devuelve la cadena con todos los caracteres en minuscula. 

print("Hola Mundo".lower())

#capitalize(): Devuelve la cadena con su primer caracter en mayuscula. 

print("hola mundo".capitalize())

#title(): Devuelve la cadena con el primer caracter de cada palabra en mayuscula. 

print("hola mundo".title())

#count(): Devuelve la cantidad de veces que aparece una subcadena en la cadena. 

print("Hola mundo".count("mundo"))

#find(): Devuelve el indice en el que aparece la subcadena (-1 si no aparece)

print("Hola Mundo".find("mundo"))

#rfind(): Devuelve el indice en el que aparece la subcadena, empezando por el final. 

print("Hola mundo mundo mundo".rfind("mundo"))

#isdigit(): Devuelve True si la cadena es todos numeros, False en caso contrario. 

c = "200"
print(c.isdigit())

#isalnum(): Devuelve True si la cadena es todo numeros o caracteres alfabeticos. 
print("11122fffff".isalnum())

#isalpha(): Devuelve True si la cadena es todo caraceres alfabeticos. 
print("FFFSDSDSDSD".isalpha())

#islower(): Devuelve True si la cadena es toda minuscula. 
print("hola mundo".islower())

#isupper(): Devuelve Ture si la cadena es toda mayuscula. 
print("HOLA MUNDO".isupper())

#istitle(): Devuelve True si la primera letra de cada palabra es mayuscula. 
print("Hola Mundo".istitle())

#isspace(): Devuelve True si la cadena es todo espacios. 
print("       -         ".isspace())

#startwith(): Devuelve True si la cadena empieza con una subcadena. 
print("Hola mundo".startswith("mola"))

#endswith(): Devuelve True si la cadena termina con una subcadena. 
print("Hola Mundo".endswith("Mundo"))

#split(): Separa la cadena en subcadenas a partir de un separador y devuelve una lista de las subcadenas. 

print("hola,mundo,python".split(","))

#join(): Une todos los caracteres de una cadena utilizando un caracter union. 
print(",".join("hola mundo python"))

#strip(): Borra todos los espacios por delante y por detras de una cadena y la devuelve. 
print("          Hola mundo pyton        ".strip())

#Se puede indicar el caracter a borrar: 

print("-------------------Hola mundo pyton        ".strip("-"))

#replace(): Reemplaza una subcadena de una cadena por otra. 

print("Hola mundo".replace("o","0"))
