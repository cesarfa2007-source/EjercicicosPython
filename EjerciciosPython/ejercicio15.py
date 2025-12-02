mayores = 0
menores = 0
while True:
    edad = input("Ingrese la edad (o 'salir' para terminar): ")
    if edad.lower() == 'salir':
        break
    edad = int(edad)
    if edad >= 18:
        mayores += 1
        print("Puede ingresar al evento.")
    else:
        menores += 1
        print("No puede ingresar al evento.")
print(f"Mayores: {mayores}, Menores: {menores}")

