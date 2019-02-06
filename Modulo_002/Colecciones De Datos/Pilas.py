#Pilas: Son colecciones de elementos que únicamente permiten dos acciones: 
# 1. Añadir un elemento a la pila
# 2. Sacar un elemento de la pila

#El último elemento en entrar es el primero en salir, en inglés conocidas como estructuras LIFO (Last In First Out)

#Las podemos crear como listas normales y añadir elementos al final con el método append()

pila = [3, 4, 5]

pila.append(6)
pila.append(7)

print(pila)

#Para sacar elementos utilizamos el método .pop()
ultimo = pila.pop()

print(ultimo)
print(pila)

ultimo = pila.pop()

print(ultimo)
print(pila)

#Si hacemos .pop() de una pila vacía devuelve error, es decir, debe estar controlado.