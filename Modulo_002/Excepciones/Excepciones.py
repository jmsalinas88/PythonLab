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

#Guardando la excepción: 
#Podemos asignar la excepción a una variable: 

try:
    n = input("Introduce un numero (ex en variable): ")
    5/n
except Exception as e:
    print(type(e).__name__)

#Encadenando excepciones:
#Podemos crear multiples comprobaciones, siempre que dejemos en último lugar la excepción padre de todas (Exception, engloba cualquier tipo de error)
#Si la ponemos al principio el resto de las comprobaciones no se ejecutarían.

try:
    n = float(input("Introduce un numero: "))
    5/n
except TypeError:
    print("No se puede dividir el numero por una cadena")
except ValueError:
    print("Debe ingresar una cadena que sea un numero")
except ZeroDivisionError:
    print("No se puede dividir por cero, pruebe otro numero")
except Exception as e:
    print(type(e).__name__)

#La instrucción "raise": Podemos lanzar una excepción. 

def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error, no se permite un valor nulo")
    except ValueError:
        print("Error, no se permite un valor nulo (desde el except)")

mi_funcion()
