# Ingresos_GameStop

import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de ingresos de GameStop
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Simular navegador con cabeceras
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Obtener HTML
response = requests.get(url, headers=headers)
html = response.text

# Analizar HTML con BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Buscar todas las tablas
tables = soup.find_all("table")

# Verifica cuántas tablas hay
print(f"Se encontraron {len(tables)} tablas.")

# Extraer tabla de ingresos (usualmente la segunda)
gme_revenue = pd.read_html(str(tables[1]))[0]

# Limpieza opcional
gme_revenue.columns = ["Fecha", "Ingresos (USD)"]
gme_revenue.dropna(inplace=True)

# Mostrar resultados
print("Ingresos trimestrales de GameStop:")
print(gme_revenue.tail())
