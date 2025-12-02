import random

niveles = {
    "Nivel máximo": (90, 100),
    "Nivel medio": (75, 90),
    "Nivel regular": (50, 75),
    "Fuera de nivel": (0, 50)
}

preguntas_realizadas = int(input("Ingrese la cantidad de preguntas realizadas: "))
preguntas_correctas = random.randint(0, preguntas_realizadas)
porcentaje = (preguntas_correctas / preguntas_realizadas) * 100

for nivel, rango in niveles.items():
    if rango[0] <= porcentaje < rango[1] or (rango[0] == 90 and porcentaje == 100):
        print(f"{nivel} obtenido")
        print(f"Respuestas correctas: {preguntas_correctas}")
        print(f"Porcentaje obtenido: {porcentaje:.2f}%")
        break