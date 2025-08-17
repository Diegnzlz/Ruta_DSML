import json
import requests
import pandas as pd
import sqlite3
import json
from sklearn.datasets import fetch_california_housing

# Realiza al menos:

# Tres consultas SQL distintas (simple, con filtro y agrupada).

data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["MedHouseVal"] = data.target

conn = sqlite3.connect("/mnt/data/housing.db")
df.to_sql("casas", conn, if_exists="replace", index=False)


# Consulta SQL básica
query_simple = """
SELECT 
    MedInc AS IngresoMedio,
    HouseAge AS EdadCasa,
    AveRooms AS HabitacionesPromedio,
    MedHouseVal AS ValorMedioCasa
FROM casas 
LIMIT 8;
"""
df_sql = pd.read_sql_query(query_simple, conn)
print(df_sql.head())

# Consulta con filtro
query_filtro = """
SELECT 
    MedInc AS IngresoMedio,
    AveRooms AS HabitacionesPromedio,
    AveBedrms AS DormitoriosPromedio,
    MedHouseVal AS ValorMedioCasa,
    Latitude,
    Longitude
FROM casas 
WHERE 
    MedInc > 8 
    AND AveRooms > 6 
    AND MedHouseVal > 4.0;
"""
df_filtrado = pd.read_sql_query(query_filtro, conn)
print(df_filtrado.head())

# Consulta agrupada
query_agrupado = """
SELECT 
    HouseAge AS EdadCasa,
    ROUND(AveOccup, 1) AS OcupacionPromedio,
    AVG(MedHouseVal) AS ValorPromedio,
    COUNT(*) AS CantidadPropiedades
FROM casas
GROUP BY EdadCasa, OcupacionPromedio
HAVING COUNT(*) > 20  -- Solo grupos significativos
ORDER BY EdadCasa DESC, ValorPromedio DESC
LIMIT 10;
"""
df_grouped = pd.read_sql_query(query_agrupado, conn)
print(df_grouped)


# Una consulta a una API pública (puede ser de clima, monedas, datos Covid, etc.) y muestra los datos en pandas.


# URL de la API (solo Estados Unidos)
url = "https://restcountries.com/v3.1/name/united%20states"

# Petición a la API
response = requests.get(url)

if response.status_code == 200:
    countries = json.loads(response.text)
    usa = countries[0]  # Solo el primer resultado (EE. UU.)
    print("Datos de EE. UU. cargados correctamente ✅")
else:
    raise Exception("Error al obtener datos de la API")

# Conexión a SQLite
conn = sqlite3.connect("california_analysis.db")
cursor = conn.cursor()

# Crear tabla de información del país
cursor.execute("""
CREATE TABLE IF NOT EXISTS pais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    nombre_oficial TEXT,
    capital TEXT,
    region TEXT,
    subregion TEXT,
    poblacion INTEGER,
    area REAL,
    fronteras TEXT
)
""")

# Insertar datos de Estados Unidos
nombre = usa.get("name", {}).get("common")
nombre_oficial = usa.get("name", {}).get("official")
capital = ", ".join(usa.get("capital", [])) if usa.get("capital") else None
region = usa.get("region")
subregion = usa.get("subregion")
poblacion = usa.get("population")
area = usa.get("area")
fronteras = ", ".join(usa.get("borders", [])) if usa.get("borders") else None

cursor.execute("""
INSERT INTO pais (nombre, nombre_oficial, capital, region, subregion, poblacion, area, fronteras)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", (nombre, nombre_oficial, capital, region, subregion, poblacion, area, fronteras))

# Guardar cambios y cerrar
conn.commit()
conn.close()

print("Datos de EE. UU. guardados en la base de datos ✅")
