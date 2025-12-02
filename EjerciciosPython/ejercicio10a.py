total_gasto = 0
for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]:
    gasto_dia = float(input(f"Ingrese el gasto diario en pasajes y refrigerio para el {dia}: "))
    total_gasto += gasto_dia
    print(f"Total semanal gastado: {total_gasto}")