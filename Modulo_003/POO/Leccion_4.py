#Herencia: 
#Es el mecanismo por el cual se pueden crear nuevas clases a partir de otras ya existentes.
#La clase base se la llama superclase o clase padre y las de jerarquía menor a esta, se denominan subclase. 
#La herencia aporta a la reutilizacion del codigo, entre otros aportes o propiedades a ser vistas mas adelante. 

""" Creando una jerarquia de productos con clase """

class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
    
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)

#Suclase Adorno. 
class Adorno(Producto):
    pass

#Subclase Alimento
class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)


#Subclase Libro
class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
ISBN\t\t{}
AUTOR\t\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)


a = Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con arboles")
print(a)

al = Alimento(2035,"Botella de Aceite de Oliva Extra",5,"250 ML")
al.productor = "La Aceitera"
al.distribuidor = "Distribuciones SA"

print(al)

li = Libro(2036,"Cocina Mediterranea",9,"Recetas sanas y buenas")
li.isbn = "0-123456-78-9"
li.autor = "Donia Juana"

print(li)