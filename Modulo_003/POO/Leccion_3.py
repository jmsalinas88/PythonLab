#Encapsulacion
#Consiste en denegar acceso directo a los atributos y metodos internos de un objeto desde el exterior. 
#Los accesos, de ser necesarios, se realizan a traves de interfases publicas definidas con ese proposito. 

class Ejemplo:
    __atributo_privado = "Atributo inalcanzable desde afuera"

    def __metodo_privado(self):
        print("Metodo inalcanzable desde afuera")

    def atributo_publico(self):
        print(self.__atributo_privado)

    def metodo_publico(self):
        self.__metodo_privado()

e = Ejemplo()

#print(e.__atributo_privado)
#e.__metodo_privado()

#Como dar accesos: 
e.atributo_publico()
e.metodo_publico()

