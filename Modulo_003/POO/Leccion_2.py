#Métodos especiales de clase
#Constructor y Destructor:

class Pelicula:

    #Constructor de objetos pelicula
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se creo la pelicula", self.titulo)

    #Destructor de clase (al borrar la instancia)
    def __del__(self):
        print("Se esta borrando", self.titulo)

    #Redefinimos el métodos string
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)
    
    #Redefinimos el metodo length
    def __len__(self):
        return self.duracion

p = Pelicula("El padrino", 120, 1972)
print(p)
print("La pelicula dura", len(p))



#Creando un catalogo de peliculas: 
class Catalogo:
    peliculas = [] #Contendra una lista de peliculas

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)

    def mostrar(self):
        for p in self.peliculas:
            print(p)

c = Catalogo([p])
c.mostrar()
