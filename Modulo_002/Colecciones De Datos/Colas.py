#Colas: Son colecciones de elementos ordenados según la inserción, permiten dos acciones: 
# 1. Añadir un elemento a la cola. 
# 2. Sacar un elemento de la cola.

#El primer elemento en entrar es el primero en salir, en inglés se conocen como estructuras FIFO (First In First Out)

from collections import deque

cola = deque()

print(cola)

print(type(cola))

#Podemos añadir elementos a la cola pasando una lista a la cola al momento de crearla: 
cola = deque(['Hector', 'Juan', 'Miguel'])

print(cola)

#También podemos agregar elementos utilizando el método .apppend()

cola.append('Maria')
cola.append('Arnaldo')

print(cola)

#Para sacar el elemento se utiliza el método .popleft() (saca por la parte izquierda, al principio de la cola)

primero = cola.popleft()

print(primero)
print(cola)

primero = cola.popleft()
print(primero)
print(cola)


