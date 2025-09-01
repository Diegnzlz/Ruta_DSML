import pandas as pd
from sklearn.datasets import fetch_california_housing

# Cargar dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

# Vista rápida
print(df.head())

# Estadísticas descriptivas
print(df.describe())

# Ejemplo de medidas
print("Media de ingresos:", df["MedInc"].mean())
print("Mediana de ingresos:", df["MedInc"].median())
print("Desviación estándar de ingresos:", df["MedInc"].std())
