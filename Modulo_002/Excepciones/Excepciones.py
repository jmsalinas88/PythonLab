#Excepciones
#Son bloques de código que nos permiten continuar con la ejecución de un programa pese a que ocurra un error. 

n = float(input("Introduce un numero: "))
m = 4
print("{}/{}={}".format(n,m,n/m))

#Si el usuario ingresa un caracter que no es numero arroja un error de conversión.

#Para prevenir el error, debemos poner el código propenso a error dentro de un bloque 'try' y el bloque 'except' para tratar la excepción. 

try:
    n = float(input("Introduce un numero: "))
    m = 4
    print("{}/{}={}".format(n,m,n/m))
except:
    print("Error al ingresar el numero")

#Bloque else de excepciones: 
#Si todo funciona bien de lo encerrado en el 'try' va a éste bloque

try:
    n = float(input("Introduce un numero: "))
    m = 4
    print("{}/{}={}".format(n,m,n/m))
except:
    print("Error al ingresar el numero")
else:
    print("Todo funciona correctamente")

#Bloque 'finally'
#Éste bloque siempre se ejecuta, ocurra o no ocurra un error. 

try:
    n = float(input("Introduce un numero: "))
    m = 4
    print("{}/{}={}".format(n,m,n/m))
except:
    print("Error al ingresar el numero")
else:
    print("Todo funciona correctamente")
finally:
    print("Siempre paso por aca")

