import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tesla_acciones import obtener_datos_acciones
from tesla_ingresos import obtener_datos_ingresos

def crear_dashboard_tesla():
    # Obtener datos de acciones e ingresos de Tesla
    datos_acciones = obtener_datos_acciones()
    datos_ingresos = obtener_datos_ingresos()

    # Configuración de la visualización
    plt.figure(figsize=(14, 7))

    # Gráfico de precios de acciones
    plt.subplot(2, 1, 1)
    plt.plot(datos_acciones['Fecha'], datos_acciones['Cierre'], label='Precio de Cierre', color='blue')
    plt.title('Precio de Acciones de Tesla')
    plt.xlabel('Fecha')
    plt.ylabel('Precio (USD)')
    plt.legend()
    plt.grid()

    # Gráfico de ingresos
    plt.subplot(2, 1, 2)
    sns.barplot(x='Fecha', y='Ingresos', data=datos_ingresos, color='orange')
    plt.title('Ingresos de Tesla')
    plt.xlabel('Fecha')
    plt.ylabel('Ingresos (USD)')
    plt.xticks(rotation=45)
    plt.grid()

    # Mostrar el dashboard
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    crear_dashboard_tesla()