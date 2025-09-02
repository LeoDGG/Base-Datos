# Tesla_Ingresos

import pandas as pd

# URL de ingresos de Tesla
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Extraer todas las tablas directamente
tables = pd.read_html(url)

# Buscar la tabla que contiene los ingresos
for i, table in enumerate(tables):
    print(f"Tabla {i}:")
    print(table.head())
    print("\n")

# Una vez identificada la tabla correcta, por ejemplo la tabla 1:
tesla_revenue = tables[1]  # Ajusta el índice según lo que veas en la salida

# Limpieza opcional
tesla_revenue.columns = ["Fecha", "Ingresos (USD)"]
tesla_revenue.dropna(inplace=True)

# Mostrar resultados
print("Ingresos trimestrales de Tesla:")
print(tesla_revenue.tail())
