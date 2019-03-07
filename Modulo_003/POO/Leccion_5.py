#Herencia multiple: 
#Es la posibilidad de que una subclase herede de multiples superclases. 
#En el caso de que las superclases tengan atributos y/o metodos comunes, Python dara prioridad a las clases mas a la izquierda en la declaracion de clases. 

class A:

    def __init__(self):
        print("Soy de clase A")

    def a(self):
        print("Este metodo lo heredo de A")

class B:

    def __init__(self):
        print("Soy de clase B")

    def b(self):
        print("Este metodo lo heredo de B")

class C(B,A):

    def c(self):
        print("Este metodo es de C")

c = C()
c.a()
c.b()
c.c()