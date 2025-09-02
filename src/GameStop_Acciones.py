# GameStop_Acciones

import yfinance as yf
import pandas as pd

# Crear objeto de GameStop
gamestop = yf.Ticker("GME")

# Extraer datos históricos (últimos 5 años)
gme_data = gamestop.history(period="5y")

# Restablecer índice para que la fecha sea una columna
gme_data.reset_index(inplace=True)

# Mostrar las primeras filas
print("Datos históricos de acciones de GameStop:")
print(gme_data.head())

