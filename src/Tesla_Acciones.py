# Tesla_Acciones

import yfinance as yf
import pandas as pd

# Crear objeto de Tesla
tesla = yf.Ticker("TSLA")

# Extraer datos históricos
tesla_data = tesla.history(period="5y")

# Restablecer índice para que la fecha sea una columna
tesla_data.reset_index(inplace=True)

# Mostrar las primeras filas
print("Datos históricos de acciones de Tesla:")
print(tesla_data.head())
