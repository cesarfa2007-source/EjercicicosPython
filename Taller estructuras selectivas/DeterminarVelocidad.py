import random

limites_velocidad = {
    "Escolar": 30,
    "Urbanas": 60,
    "Rurales": 80,
    "Nacionales": 100
}

zona_rand = random.choice(list(limites_velocidad.keys()))
velocidad = round(random.uniform(0, 200), 1)

limite = limites_velocidad[zona_rand]

if velocidad <= limite:
    mensaje = f"Estás a {velocidad} km/h en zona {zona_rand}. No infringes la norma (límite {limite} km/h)"
else:
    mensaje = f"Estás a {velocidad} km/h en zona {zona_rand}. Infringes la norma, reduce a {limite} km/h"

print(mensaje)




       
