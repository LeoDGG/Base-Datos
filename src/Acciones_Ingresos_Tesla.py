# Acciones_Ingresos_Tesla

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# --- Datos de acciones ---
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="5y")
tesla_data.reset_index(inplace=True)

# --- Datos de ingresos (simulados o previamente extraídos) ---
# Reemplaza esto con tu DataFrame real si ya hiciste el web scraping
tesla_revenue = pd.DataFrame({
    "Fecha": pd.date_range(start="2020-01-01", periods=20, freq="Q"),
    "Ingresos (USD)": [5 + i*0.5 for i in range(20)]
})

# --- Crear figura y ejes ---
fig, ax1 = plt.subplots(figsize=(12,6))  # ← Esta línea define ax1 correctamente

# Gráfico de precio de acciones
ax1.plot(tesla_data["Date"], tesla_data["Close"], label="Precio de Cierre", color="blue")
ax1.set_xlabel("Fecha")
ax1.set_ylabel("Precio de acciones (USD)", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Segundo eje para ingresos
ax2 = ax1.twinx()
ax2.plot(tesla_revenue["Fecha"], tesla_revenue["Ingresos (USD)"], label="Ingresos", color="green", linestyle="--")
ax2.set_ylabel("Ingresos (USD en miles de millones)", color="green")
ax2.tick_params(axis="y", labelcolor="green")

# Título y leyenda
plt.title("Tablero de Tesla: Precio de acciones vs Ingresos")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.grid(True)
plt.tight_layout()
plt.show()
