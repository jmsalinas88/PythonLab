#If: Permite dividir el flujo de un programa en diferentes caminos: 
if True: 
    print("Se cumple la condicion")
    print("Tambien se muestra este print")

a = 5 
if a == 5:
    print("a vale 5")
if a == 2: 
    print("a vale 2")

#Anidar if dentro de if: 
a = 5
b = 10 
if a == 5: 
    print("a vale", 5)
    if b == 10:
        print("y b vale", b)

#Evaluar múltiples expresiones: 
if a == 5 and b == 10:
    print("a vale 5 y b vale 10")

#Sentencia else (Sino): 
n = 11
if n % 2 == 0:
    print(n, "es un número par")
else:
    print(n,"es un número impar")

#Sentencia elif (Sino si):
commando = "OTRA COSA"
if commando == "ENTRAR":
    print("Bienvenido al sistema")
elif commando == "SALUDAR":
    print("Hola")
elif commando == "SALIR":
    print("Saliendo del sistema")
else:
    print("Este comando no se reconoce")

