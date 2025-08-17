import json
import requests
import sqlite3
import pandas as pd
from sklearn.datasets import fetch_california_housing

# ---------------------------------------------
# 1. Cargar y guardar dataset de California
# ---------------------------------------------
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)  # type: ignore
df["MedHouseVal"] = data.target  # type: ignore

conn = sqlite3.connect("/mnt/data/housing.db")
df.to_sql("casas", conn, if_exists="replace", index=False)

# ---------------------------------------------
# 2. Consultas SQL sobre la tabla 'casas'
# ---------------------------------------------
query_simple = """
SELECT
    MedInc AS IngresoMedio,
    HouseAge AS EdadCasa,
    AveRooms AS HabitacionesPromedio,
    MedHouseVal AS ValorMedioCasa
FROM casas
LIMIT 8;
"""
print("Consulta simple (primeros 8 registros):")
print(pd.read_sql_query(query_simple, conn), "\n")

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
print("Consulta con filtro (alta calidad e ingresos):")
print(pd.read_sql_query(query_filtro, conn), "\n")

query_agrupado = """
SELECT
    HouseAge AS EdadCasa,
    ROUND(AveOccup, 1) AS OcupacionPromedio,
    AVG(MedHouseVal) AS ValorPromedio,
    COUNT(*) AS CantidadPropiedades
FROM casas
GROUP BY EdadCasa, OcupacionPromedio
HAVING CantidadPropiedades > 20
ORDER BY EdadCasa DESC, ValorPromedio DESC
LIMIT 10;
"""
print("Consulta agrupada (valor promedio por edad de casa y ocupación):")
print(pd.read_sql_query(query_agrupado, conn), "\n")

# ---------------------------------------------
# 3. Extraer información de EE.UU. desde API
# ---------------------------------------------
url = "https://restcountries.com/v3.1/name/united%20states"
response = requests.get(url)

if response.status_code == 200:
    countries = json.loads(response.text)
    usa = countries[0]
    print("Datos de EE. UU. cargados desde la API correctamente.\n")
else:
    raise Exception("Error al obtener datos de la API")

# ---------------------------------------------
# 4. Guardar los datos de EE. UU. en SQLite
# ---------------------------------------------
conn2 = sqlite3.connect(
    "Fase1_Data_Scientist_Junior/Modulo6_BaseDeDatos/california_analysis.db")
cursor = conn2.cursor()

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

nombre = usa.get("name", {}).get("common")
nombre_oficial = usa.get("name", {}).get("official")
capital = ", ".join(usa.get("capital", [])) if usa.get("capital") else None
region = usa.get("region")
subregion = usa.get("subregion")
poblacion = usa.get("population")
area = usa.get("area")
fronteras = ", ".join(usa.get("borders", [])) if usa.get("borders") else None

cursor.execute("""
INSERT INTO pais (
    nombre, nombre_oficial, capital, region, subregion,
    poblacion, area, fronteras
) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", (nombre, nombre_oficial, capital, region, subregion, poblacion, area, fronteras))

conn2.commit()
conn2.close()

# Cerrar conexión original
conn.close()

print("Datos de EE. UU. guardados en la base de datos correctamente.")
