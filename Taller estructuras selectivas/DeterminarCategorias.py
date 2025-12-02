print("\n-------- Determinar Categorias por Edad ------\n")
edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Edad invalida")
elif 0 <= edad <= 5:
    print ("La categoria de esa edad es: infante ")
elif 6 <= edad <= 10:
    print ("La categoria de esa edad es: niño ")
elif 11 <= edad <= 15:
    print ("La categoria de esa edad es: pre adolecente ")
elif 16 <= edad <= 18:
    print ("La categoria de esa edad es: adolecente ")
elif 19 <= edad <= 25:
    print ("La categoria de esa edad es: pre adulto ")
elif 26 <= edad <= 40:
    print ("La categoria de esa edad es: adulto")
elif 41 <= edad <= 55:
    print ("La categoria de esa edad es: pre anciano ")
else:
    print ("La categoria de esa edad es: Anciano")