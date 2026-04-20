import json
import matplotlib.pyplot as plt
import csv
import os
from datetime import datetime

# Charger JSON
with open('../data/meteo.json') as f:
    data = json.load(f)

# Vérifier erreur API
if 'main' not in data:
    print("❌ Erreur API :", data.get('message', 'Inconnue'))
    exit(1)

temp = data['main']['temp']
humidity = data['main']['humidity']
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

csv_file = '../data/historique_meteo.csv'

# 📥 Sauvegarde dans CSV
file_exists = os.path.isfile(csv_file)

with open(csv_file, 'a', newline='') as f:
    writer = csv.writer(f)
    
    # Ajouter header si fichier vide
    if not file_exists:
        writer.writerow(['date', 'temperature', 'humidity'])
    
    writer.writerow([date, temp, humidity])

print("✅ Données ajoutées au CSV")

# 📊 Lire CSV pour graphique
dates = []
temps = []
humidities = []

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        dates.append(row['date'])
        temps.append(float(row['temperature']))
        humidities.append(float(row['humidity']))

# 📈 Graphique (2 courbes)
plt.figure()

plt.plot(dates, temps, marker='o', label='Température (°C)')
plt.plot(dates, humidities, marker='o', label='Humidité (%)')

plt.xticks(rotation=45)
plt.xlabel("Temps")
plt.ylabel("Valeurs")
plt.title("Évolution météo")
plt.legend()

plt.tight_layout()
plt.savefig('../output/meteo.png')

# 📄 Rapport texte
with open('../output/rapport.txt', 'w') as f:
    f.write("=== RAPPORT METEO ===\n\n")
    f.write(f"Dernière mesure:\n")
    f.write(f"Température: {temp} °C\n")
    f.write(f"Humidité: {humidity} %\n")

print("✅ Graphique mis à jour")
