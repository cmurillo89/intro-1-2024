#HOY HABLAREMOS DE LOS BUCLES
#LOS BUCLES SIRVEN PARA REPETIR UNA ACCIÓN VARIAS VECES

#FOR
#El bucle for es un bucle que se repite un número determinado de veces

for i in range(10):
    print(i)

wallet = 1000

for i in range(100):
    wallet = wallet +100
    print("wallet: ", wallet)
    print("i: ", i)

#WHILE
#El bucle while se repite mientras una condición sea verdadera
    
print("WHILE-----------------")


while False:
    print("Continuando...")
    continuar = input("Desea continuar? (s/n): ")
    if continuar == "n":
        print("Saliendo del bucle while")
        break
    elif continuar != "s":
        print("Opción incorrecta")
        continuar = input("Desea continuar? (s/n): ")

num_oculto = 25

while True:
    numero = int(input("Ingrese un número: "))
    if numero == num_oculto:
        print("Adivinaste el número oculto")
        break
    else:
        print("Número incorrecto")


print("Fin del programa")

#EJERCICIO

contrasena = "1234"
intentos = 0
while True:
    clave = input("Ingrese la contraseña: ")
    if clave == contrasena:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
        intentos += 1
        print("Intentos: ", intentos)
        if intentos == 3:
            print("Demasiados intentos")
            break