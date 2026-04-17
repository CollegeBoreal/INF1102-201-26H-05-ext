import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dotenv import load_dotenv

# === Chargement des chemins ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

CSV_PATH = os.path.join(DATA_DIR, "prices.csv")
GRAPH_PATH = os.path.join(OUTPUT_DIR, "graph.png")
RAPPORT_PATH = os.path.join(OUTPUT_DIR, "rapport.txt")

# === Chargement API KEY ===
load_dotenv()
API_KEY = os.getenv("CRYPTO_API_KEY")

if not API_KEY:
    raise Exception("Clé API manquante")

# === EXTRACTION ===
url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin", "vs_currencies": "usd"}
response = requests.get(url, params=params)
price = response.json()["bitcoin"]["usd"]

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# === LOAD ===
new_row = pd.DataFrame([[timestamp, price]], columns=["timestamp", "price"])

if os.path.exists(CSV_PATH) and os.path.getsize(CSV_PATH) > 0:
    df = pd.read_csv(CSV_PATH)
    df = pd.concat([df, new_row], ignore_index=True)
else:
    df = new_row

df.to_csv(CSV_PATH, index=False)

# === VISUALISATION ===
df["timestamp"] = pd.to_datetime(df["timestamp"])
plt.figure()
plt.plot(df["timestamp"], df["price"])
plt.xlabel("Temps")
plt.ylabel("Prix BTC (USD)")
plt.title("Évolution du prix du Bitcoin")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(GRAPH_PATH)
plt.close()

# === RAPPORT TEXTE ===
with open(RAPPORT_PATH, "w", encoding="utf-8") as f:
    f.write("Rapport d’analyse crypto\n")
    f.write(f"Date : {timestamp}\n")
    f.write(f"Prix du Bitcoin : {price} USD\n")

print("Analyse complétée avec Succes")

