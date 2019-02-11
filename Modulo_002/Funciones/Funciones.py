#Funciones: Son fragmentos de código que realizar una tarea y devuelven un valor, puede recibir argumentos o no. 

#Definición y llamada: 
def saludar():
    print("Hola, esto es un saludo")

saludar()

#Dentro de una función podemos usar variables y sentencias de control. 

def dibujar_tabla_de_5():
    for i in range(10):
        print("5 * {} = {}".format(i, i*5))

dibujar_tabla_de_5()


#Retorno de valores: 
#Para comunicarse con el exterior, las funciones pueden devolver valores mediante la instrucción "return"

def test():
    return "Una cadena de retorno"

print(test())

#Retorno múltiple: La posibilidad de devolver multiples valores separados por comas. 

def testMultiple():
    return "Una cadena", 20, [1,2,3]

print(testMultiple())

#Ésos valores se tratan como una tupla inmutable, se puede reasignar a distintas variables. 

#Envío de valores: Para comunicarse con el exterior, las funciones no sólo puede devolver valores, también pueden recibir información. 
def sumar(a, b):
    return a + b
print(sumar(100, 200))

r = sumar(10, 20)
print(r)

#Argumentos por posición: Se envían los argumentos de acuerdo a la posición de los parámetros. 

def restar(a, b):
    return a - b

a = 10
b = 5

print(restar(a,b))

#Argumentos por nombre: Se envían los argumentos de acuerdo a los nombres de los parámetros. 
print(restar(a=10, b=2))

#Parámetros por defecto: 
def resta_con_default(a=None, b=None):
    r = None
    if a == None or b == None:
        print("Error, debés enviar dos números a la función")
    else:
        r = a - b
    return r

print(resta_con_default(10,4))

