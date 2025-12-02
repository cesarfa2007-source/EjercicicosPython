horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))
salario = horas_trabajadas * valor_hora
if horas_trabajadas > 40:
    extra = (horas_trabajadas - 40) * valor_hora * 0.5
    salario += extra
print(f"Salario total: {salario}")

