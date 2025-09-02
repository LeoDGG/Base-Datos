import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from gamestop_ingresos import obtener_ingresos_gamestop

def graficar_acciones_gamestop():
    # Obtener datos de acciones de GameStop
    gamestop_data = yf.download('GME', start='2020-01-01', end='2023-01-01')
    
    # Graficar el precio de cierre
    plt.figure(figsize=(14, 7))
    plt.plot(gamestop_data['Close'], label='Precio de Cierre', color='blue')
    plt.title('Precio de Cierre de GameStop')
    plt.xlabel('Fecha')
    plt.ylabel('Precio (USD)')
    plt.legend()
    plt.grid()
    plt.show()

def graficar_ingresos_gamestop():
    # Obtener datos de ingresos de GameStop
    ingresos = obtener_ingresos_gamestop()
    
    # Graficar ingresos
    plt.figure(figsize=(14, 7))
    sns.barplot(x='Año', y='Ingresos', data=ingresos, palette='viridis')
    plt.title('Ingresos Anuales de GameStop')
    plt.xlabel('Año')
    plt.ylabel('Ingresos (USD)')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

def main():
    graficar_acciones_gamestop()
    graficar_ingresos_gamestop()

if __name__ == "__main__":
    main()