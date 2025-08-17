import requests
import pandas as pd
import sqlite3
from sklearn.datasets import fetch_california_housing

# Cargar dataset California Housing
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["MedHouseVal"] = data.target

# Crear conexión SQLite y guardar la tabla
conn = sqlite3.connect("/mnt/data/housing.db")
df.to_sql("casas", conn, if_exists="replace", index=False)

# Consulta SQL básica
query = "SELECT * FROM casas LIMIT 3;"
df_sql = pd.read_sql_query(query, conn)
print(df_sql.head())

# Consulta con filtro
query = "SELECT HouseAge, MedHouseVal FROM casas WHERE HouseAge > 10;"
df_filtrado = pd.read_sql_query(query, conn)
print(df_filtrado.head())

# Consulta agrupada
query = "SELECT HouseAge, AVG(MedHouseVal) as ValorPromedio FROM casas GROUP BY HouseAge ORDER BY ValorPromedio DESC LIMIT 5;"
df_grouped = pd.read_sql_query(query, conn)
print(df_grouped)
