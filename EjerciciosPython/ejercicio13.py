positivos = 0
negativos = 0
for _ in range(5):
    num = int(input("Ingrese un número: "))
    if num >= 0:
        positivos += 1
    else:
        negativos += 1
print(f"Positivos: {positivos}, Negativos: {negativos}")

