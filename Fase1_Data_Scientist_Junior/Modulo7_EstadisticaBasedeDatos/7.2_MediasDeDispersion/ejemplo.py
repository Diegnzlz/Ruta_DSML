import pandas as pd
from sklearn.datasets import fetch_california_housing

# Cargar el dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

# --- Varianza y Desviación Estándar ---
print("Varianza de HouseAge:", df["HouseAge"].var())
print("Desviación estándar de HouseAge:", df["HouseAge"].std())

# --- Rango ---
print("Rango de HouseAge:", df["HouseAge"].max() - df["HouseAge"].min())

# --- Percentiles ---
print("Percentiles de HouseAge:")
print(df["HouseAge"].quantile([0.25, 0.5, 0.75]))
