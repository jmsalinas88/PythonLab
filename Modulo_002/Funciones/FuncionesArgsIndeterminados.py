#Argumentos y parámetos indeterminados 
#Cuando no sabemos de antemano cuántos elementos le vamos a mandar a una función, podemos utilizar los parámetros indeterminados por posición y por nombre. 

#Por posición
def indeterminados_posicion(*args):
    for arg in args:
        print(arg)
    
indeterminados_posicion(5,"Hola",[1,2,3,4,5])

#Por nombre
#Se debe crear un diccionario dinámico de argumentos

def indeterminados_posicion_dic(**kwargs):
        print(kwargs)

    
indeterminados_posicion_dic(a=5,b="Hola",c=[1,2,3,4,5])

def indeterminados_posicion_dic_vals(**kwargs):
    for kwarg in kwargs:
        print(kwarg, " ", kwargs[kwarg])

indeterminados_posicion_dic_vals(a=5,b="Hola",c=[1,2,3,4,5])

#Por posición y por nombre a la vez
def super_funcion(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, " ", kwargs[kwarg])

super_funcion(1, 2, ["hola", "que", "tal"], nombre="Juan", apellido="Salinas")