import datetime

sucursal = "911"

print("Bienvenido al sistema de atención del banco.")

Continuar = input("Desea continuar con la operación? (s/n): ").lower()
    
if Continuar == "s":

    cedula = input("Ingrese su número de cédula: ")
    nombre = input("Ingrese su nombre: ")

    print("¡MENÚ DE SERVICIOS!")
    print("1. Servicio de Caja")
    print("2. Servicio al Cliente")
    print("3. Pago de Impuestos")
    print("4. Crédito Hipotecario")
    print("5. Tarjeta de Crédito")
    
    
    opcion = int(input("Seleccione una opción: "))
    
    servicio = ""

    if opcion == 1:
        servicio = "Servicio de caja"
    else:
        if opcion == 2:
            servicio = "Servicio al cliente"
        else:
            if opcion == 3:
                servicio = "Pago de impuestos"
            else:
                if opcion == 4:
                    servicio = "Crédito hipotecario"
                else:
                    if opcion == 5:
                        servicio = "Operaciones con tarjeta de crédito"
                    else:
                        print("Opción no válida. Ticket cancelado.")
                        servicio = None
        
    if servicio is not None:
        fecha = datetime.datetime.now().strftime("%d/%m/%Y")

        print("TICKET GENERADO")
        print(f"Sucursal ID: {sucursal}")
        print(f"Nombre: {nombre}")
        print(f"Cédula: {cedula}")
        print(f"Servicio: {servicio}")
        print(f"Fecha: {fecha}")
else:
    print("Operación cancelada por el usuario.")