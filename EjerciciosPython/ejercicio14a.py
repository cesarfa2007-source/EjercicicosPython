total_semanal = 0
for dia in range(1, 6):
    horas_trabajadas = float(input(f"Ingrese las horas trabajadas el día {dia}: "))
    valor_hora = float(input(f"Ingrese el valor por hora el día {dia}: "))
    salario_dia = horas_trabajadas * valor_hora
    if horas_trabajadas > 8:  # Suponiendo 8 horas normales por día
        extra = (horas_trabajadas - 8) * valor_hora * 0.5
        salario_dia += extra
        total_semanal += salario_dia
print(f"Salario total semanal: {total_semanal}")

