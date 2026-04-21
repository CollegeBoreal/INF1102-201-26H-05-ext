#!/usr/bin/env python3
# ============================================
# analyse.py — Analyse des données météo
# Étudiant : Hani Damouche (300150557)
# Cours : INF1102 — Programmation système
# ============================================

import sys
import json
import os
from datetime import datetime

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("⚠️  matplotlib non installé — graphiques désactivés")
def charger_donnees(fichier):
    """Charge les données JSON depuis le fichier"""
    with open(fichier, 'r', encoding='utf-8-sig') as f:
        return json.load(f)
def analyser(data):
    """Extrait les statistiques principales"""
    stats = {
        'ville': data.get('name', 'Inconnue'),
        'pays': data.get('sys', {}).get('country', 'N/A'),
        'temperature': data['main']['temp'],
        'ressenti': data['main']['feels_like'],
        'temp_min': data['main']['temp_min'],
        'temp_max': data['main']['temp_max'],
        'humidite': data['main']['humidity'],
        'pression': data['main']['pressure'],
        'vent': data['wind']['speed'],
        'description': data['weather'][0]['description'],
        'date': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    return stats

def generer_rapport(stats, output_dir):
    """Génère le rapport texte"""
    rapport = f"""
=================================================
     RAPPORT MÉTÉO — {stats['ville']}, {stats['pays']}
=================================================
📅 Date : {stats['date']}

🌡️  Température    : {stats['temperature']} °C
🤒 Ressenti       : {stats['ressenti']} °C
⬇️  Minimum        : {stats['temp_min']} °C
⬆️  Maximum        : {stats['temp_max']} °C
💧 Humidité       : {stats['humidite']} %
🌬️  Vent           : {stats['vent']} m/s
📊 Pression       : {stats['pression']} hPa
☁️  Conditions     : {stats['description']}

=================================================
"""
    fichier_rapport = os.path.join(output_dir, 'rapport.txt')
    with open(fichier_rapport, 'w', encoding='utf-8') as f:
        f.write(rapport)
    print(f"✅ Rapport généré : {fichier_rapport}")
    print(rapport)

def generer_graphique(stats, output_dir):
    """Génère un graphique des données météo"""
    if not HAS_MATPLOTLIB:
        return

    categories = ['Temp.', 'Ressenti', 'Min', 'Max', 'Humidité']
    valeurs = [
        stats['temperature'],
        stats['ressenti'],
        stats['temp_min'],
        stats['temp_max'],
        stats['humidite']
    ]
    couleurs = ['#FF6B6B', '#FF8E53', '#4ECDC4', '#45B7D1', '#96CEB4']

    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, valeurs, color=couleurs, edgecolor='black')
    plt.title(f"Météo — {stats['ville']} ({stats['date']})", fontsize=14, fontweight='bold')
    plt.ylabel("Valeur (°C / %)")
    plt.grid(axis='y', alpha=0.3)

    for bar, val in zip(bars, valeurs):
        plt.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
                 f'{val}', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    fichier_graph = os.path.join(output_dir, 'meteo.png')
    plt.savefig(fichier_graph, dpi=150)
    plt.close()
    print(f"✅ Graphique généré : {fichier_graph}")

# === MAIN ===
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python3 analyse.py <fichier_json>")
        sys.exit(1)

    fichier = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, '..', 'output')

    print(f"📂 Chargement de {fichier}...")
    data = charger_donnees(fichier)

    print("📊 Analyse en cours...")
    stats = analyser(data)

    generer_rapport(stats, output_dir)
    generer_graphique(stats, output_dir)

    print("=== Analyse terminée ===")