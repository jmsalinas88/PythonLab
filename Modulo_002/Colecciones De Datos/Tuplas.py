#Tuplas: Son colecciones parecidas a las listas, con la diferencia de que son inmutables. 

tupla = (100, "Hola", [1,2,3], -50)

print(tupla)

#Indexación y slicing: 
print(tupla[0])

print(tupla[-1])

print(tupla[:2])

#Función len(): me indica la cantidad de elementos de la tupla
print(len(tupla))

#Métodos integrados
#index(): Sirve para buscar un elemento y saber su posición en la tupla. Da error si no se encuentra

print(tupla.index(100))

#print(tupla.index("Chau"))

#count(): Sirve para contar cuántas veces aparece un elemento en la tupla

print(tupla.count(100))

print(tupla.count("Chau"))