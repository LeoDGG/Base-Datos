# Proyecto de Análisis de Datos

Este proyecto tiene como objetivo la extracción y visualización de datos de acciones e ingresos de las empresas Tesla y GameStop. Utiliza técnicas de web scraping y la biblioteca `yfinance` para obtener información relevante y presenta los resultados a través de cuadros de mando.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
proyecto-analisis-datos
├── src
│   ├── tesla_acciones.py         # Extracción de datos de acciones de Tesla
│   ├── tesla_ingresos.py         # Extracción de datos de ingresos de Tesla mediante web scraping
│   ├── gamestop_acciones.py      # Extracción de datos de acciones de GameStop
│   ├── gamestop_ingresos.py      # Extracción de datos de ingresos de GameStop mediante web scraping
│   ├── dashboard_tesla.py         # Cuadro de mando para visualizar datos de Tesla
│   ├── dashboard_gamestop.py      # Cuadro de mando para visualizar datos de GameStop
│   └── utils
│       └── helpers.py             # Funciones auxiliares para el proyecto
├── requirements.txt               # Dependencias del proyecto
├── README.md                      # Documentación del proyecto
└── tareas.ipynb                   # Cuaderno de Jupyter para análisis interactivo
```

## Instalación

Para instalar las dependencias necesarias, ejecute el siguiente comando:

```
pip install -r requirements.txt
```

## Ejecución

1. Para extraer datos de acciones de Tesla, ejecute:
   ```
   python src/tesla_acciones.py
   ```

2. Para extraer datos de ingresos de Tesla, ejecute:
   ```
   python src/tesla_ingresos.py
   ```

3. Para extraer datos de acciones de GameStop, ejecute:
   ```
   python src/gamestop_acciones.py
   ```

4. Para extraer datos de ingresos de GameStop, ejecute:
   ```
   python src/gamestop_ingresos.py
   ```

5. Para visualizar los datos de Tesla, ejecute:
   ```
   python src/dashboard_tesla.py
   ```

6. Para visualizar los datos de GameStop, ejecute:
   ```
   python src/dashboard_gamestop.py
   ```

## Uso del Cuaderno de Jupyter

El archivo `tareas.ipynb` permite realizar análisis interactivos y visualizar los resultados de las extracciones de datos y los dashboards. Puede abrirlo utilizando Jupyter Notebook o Jupyter Lab.

## Contribuciones

Las contribuciones son bienvenidas. Si desea mejorar este proyecto, siéntase libre de hacer un fork y enviar un pull request.