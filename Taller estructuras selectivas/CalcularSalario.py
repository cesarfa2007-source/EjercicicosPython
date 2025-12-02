
horas_trabajadas = int(input("Ingrese el número de horas trabajadas en la semana: "))
valor_hora = 6471
    


salario_bruto_semanal = horas_trabajadas * valor_hora
salario_bruto_mensual = salario_bruto_semanal * 4
deduccion_emi = salario_bruto_mensual * 0.03  
salario_minimo = 1423500
auxilio_transporte = 0 if salario_bruto_mensual < (salario_minimo * 2) else None  
retencion_alimentos = salario_bruto_mensual * 0.30 if salario_bruto_mensual > 3740000 else 0
aporte_fondo_empleados = salario_bruto_mensual * 0.05
salario_neto = salario_bruto_mensual - deduccion_emi - retencion_alimentos - aporte_fondo_empleados

print("                    ")
print(f"--- Resultados ---")
print(f"Salario Bruto Mensual: ${salario_bruto_mensual:,.2f}")
print(f"Deducción EMI: ${deduccion_emi:,.2f}")
print(f"Retención por alimentos: ${retencion_alimentos:,.2f}")
print(f"Aporte al fondo de empleados: ${aporte_fondo_empleados:,.2f}")
print(f"Salario Neto: ${salario_neto:,.2f}")
if auxilio_transporte is not None:
    print("Auxilio de transporte: No aplica")
else:
    print("Auxilio de transporte: Se cancela")

