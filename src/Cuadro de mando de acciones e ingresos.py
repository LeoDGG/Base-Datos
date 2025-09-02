# Cuadro de mando de acciones e ingresos de GameStop

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Extraer datos de acciones de GameStop
gme = yf.Ticker("GME")
gme_data = gme.history(period="5y")
gme_data.reset_index(inplace=True)

# Simular ingresos trimestrales (reemplaza con tus datos reales)
gme_revenue = pd.DataFrame({
    "Fecha": pd.date_range(start="2020-01-01", periods=20, freq="Q"),
    "Ingresos (USD)": [1.5 + i*0.1 for i in range(20)]
})

# Crear gráfico
fig, ax1 = plt.subplots(figsize=(12,6))
ax1.plot(gme_data["Date"], gme_data["Close"], label="Precio de Cierre (GME)", color="red")
ax1.set_xlabel("Fecha")
ax1.set_ylabel("Precio de acciones (USD)", color="red")
ax1.tick_params(axis="y", labelcolor="red")

ax2 = ax1.twinx()
ax2.plot(gme_revenue["Fecha"], gme_revenue["Ingresos (USD)"], label="Ingresos trimestrales", color="purple", linestyle="--")
ax2.set_ylabel("Ingresos (USD en miles de millones)", color="purple")
ax2.tick_params(axis="y", labelcolor="purple")

plt.title("Tablero de GameStop: Precio de acciones vs Ingresos")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.grid(True)
plt.tight_layout()
plt.show()
