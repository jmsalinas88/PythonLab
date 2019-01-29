#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Asignacion de un valor a una variable: 
a = 1

#Trabajando con numeros

#Division
a = 100
b = 2
resultado = a / b
print("El resultado de dividir", a, "por", b, "es:", resultado)

#Modulo
a = 3
b = 2
resultado = a%b 
print("El modulo de",a, "entre", b, "es:",resultado)

#Potencia
a = 3
b = 2
resultado = a**b
print("La potencia de", a, "a la", b, "es:", resultado)

#Podemos distinguir dos tipo de numeros: 
#Enteros: No tienen una parte decimal, val desde el -infinito hasta el + infnito. 
#Flotantes o Decimales: Tienen una parte decimal escrita con un punto.

#Para redondear la parte decimal de un numero flotante se utiliza: "%.2f" % a
a = 100000
b = 38.7
resultado = a / b
print("Con parte decimal, mas de 2 digitos:",resultado)
print("El resultado es","%.2f"%resultado)  

