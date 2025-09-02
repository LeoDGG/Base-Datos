import requests
from bs4 import BeautifulSoup

def obtener_ingresos_gamestop():
    url = "https://www.example.com/gamestop-ingresos"  # Reemplazar con la URL real
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Aquí se debe ajustar el selector según la estructura de la página
        ingresos = soup.find_all('div', class_='ingresos-clase')  # Reemplazar con la clase real
        
        datos_ingresos = []
        for ingreso in ingresos:
            año = ingreso.find('span', class_='año-clase').text  # Reemplazar con la clase real
            monto = ingreso.find('span', class_='monto-clase').text  # Reemplazar con la clase real
            datos_ingresos.append({'año': año, 'monto': monto})
        
        return datos_ingresos
    else:
        print("Error al acceder a la página:", response.status_code)
        return None

if __name__ == "__main__":
    ingresos_gamestop = obtener_ingresos_gamestop()
    print(ingresos_gamestop)