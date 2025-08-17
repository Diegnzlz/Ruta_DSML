import requests
import pandas as pd

# Consulta básica a una API pública (ejemplo: Open-Meteo)
url = "https://api.open-meteo.com/v1/forecast?latitude=10.5&longitude=-66.9&current_weather=true"
response = requests.get(url)
data = response.json()
print(data["current_weather"])

# Convertir datos a DataFrame (si la estructura lo permite)
df_api = pd.DataFrame([data["current_weather"]])
print(df_api)
