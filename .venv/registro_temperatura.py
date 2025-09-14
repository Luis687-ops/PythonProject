# registro_temperaturas.py
import json
import random

cities = ["Quito", "Guayaquil", "Cuenca"]
days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_weeks = 2
random.seed(42)

# Crear matriz 3D: temps[ciudad][semana][dia]
temps = []
for _ in range(len(cities)):
    city_weeks = []
    for _ in range(num_weeks):
        week_days = [round(random.uniform(15, 35), 1) for _ in range(len(days))]
        city_weeks.append(week_days)
    temps.append(city_weeks)

# Calcular promedios e imprimir
for c_idx, city in enumerate(cities):
    print(f"Ciudad: {city}")
    for w_idx in range(num_weeks):
        week_values = temps[c_idx][w_idx]
        avg = sum(week_values) / len(week_values)
        day_temps = ", ".join(f"{day}: {t}°C" for day, t in zip(days, week_values))
        print(f"  Semana {w_idx+1} - temperaturas: {day_temps}")
        print(f"    Promedio semana {w_idx+1}: {avg:.2f} °C")
    print()

# (Opcional) guardar datos en JSON para subir al repo
with open("temperaturas_datos.json", "w", encoding="utf-8") as f:
    json.dump({
        "cities": cities,
        "days": days,
        "num_weeks": num_weeks,
        "temps": temps
    }, f, ensure_ascii=False, indent=2)
