import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener clave API desde entorno
api_key = os.getenv('WEATHER_API_KEY')
ciudad = 'Puerto Montt'
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}&aqi=no&lang=es'

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    fecha = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    archivo = f'weather_{ciudad.replace(" ", "_")}_{fecha}.json'

    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✅ Archivo guardado exitosamente como '{archivo}'")

except requests.exceptions.RequestException as e:
    print("❌ Error al hacer la solicitud:", e)
