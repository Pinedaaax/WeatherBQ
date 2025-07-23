import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Cargar claves del archivo .env
load_dotenv()
api_key = os.getenv('WEATHER_API_KEY')

# Configuración
ciudad = 'Puerto Montt'
ayer = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={ciudad}&dt={ayer}&lang=es"

# Consulta a la API
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    archivo = f"weather_historico_{ciudad.replace(' ', '_')}_{ayer}.json"
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✅ Datos históricos guardados como '{archivo}'")

except requests.exceptions.RequestException as e:
    print("❌ Error al hacer la solicitud:", e)
