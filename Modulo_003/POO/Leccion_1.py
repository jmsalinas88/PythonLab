#Una clase es un molde para crear objetos. 
#Definición de clase: 

"""class Galleta:
    pass """ 
 
#Instanciación: 
"""una_galleta = Galleta()"""
"""otra_galleta = Galleta()"""

#Atributos y métodos de clase:
#Atributos: hacen referencia a las variables internas de la clase. 
#Métodos: Hacen referencia a las funciones de la clase, pueden ser privadas o públicas. 

class Galleta:
    chocolate = False #Atributo de clase
    
     # Se llama automaticamente al crear una instancia de clase. 'self' sirve para hacer referencia a los metodos y atributos de una clase.
     # Diferencia de las variables locales de las funciones. Los 'None' son los valores por defecto de los argumentos.
    def __init__(self, sabor=None, forma=None):
        self.sabor = sabor
        self.forma = forma

    def chocolatear(self): #Defino un método de instancia. 'self' para manejar el objeto. 
        self.chocolate = True
    

