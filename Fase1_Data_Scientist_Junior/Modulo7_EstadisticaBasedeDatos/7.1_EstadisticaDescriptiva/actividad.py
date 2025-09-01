import pandas as pd
from sklearn.datasets import fetch_california_housing

# Cargar el dataset de California Housing
data = fetch_california_housing(as_frame=True)
df = data.frame

print("Primeras filas del dataset:")
print(df.head(), "\n")

# Media y mediana de HouseAge
media_house_age = df["HouseAge"].mean()
mediana_house_age = df["HouseAge"].median()

print(f"Media de HouseAge: {media_house_age:.2f}")
print(f"Mediana de HouseAge: {mediana_house_age:.2f}")

# Desviación estándar de MedHouseVal
std_house_val = df["MedHouseVal"].std()
print(f"Desviación estándar de MedHouseVal: {std_house_val:.2f}")
