import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Cargar claves desde .env
load_dotenv()
api_key = os.getenv('WEATHER_API_KEY')

# Parámetros
ciudad = 'Puerto Montt'
ayer = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={ciudad}&dt={ayer}&lang=es"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Extraer solo la parte horaria
    horas = data['forecast']['forecastday'][0]['hour']

    # Guardar en archivo JSON
    nombre_archivo = f"clima_horario_{ciudad.replace(' ', '_')}_{ayer}.json"
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        json.dump(horas, f, ensure_ascii=False, indent=4)

    print(f"✅ Archivo JSON generado: {nombre_archivo}")

except requests.exceptions.RequestException as e:
    print("❌ Error al hacer la solicitud:", e)
