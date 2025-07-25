# Lee un CSV real (puedes usar el Titanic de Kaggle o un dataset de tu interés) y:
# Muestra las 5 primeras filas.
# Calcula el promedio de edad.
# Filtra solo los pasajeros con edad menor a 18 años.

import pandas as pd
df = pd.read_csv("Fase1_Data_Scientist_Junior/Modulo2_numpypandas/train.csv")
print("Primeras 5 filas:\n", df.head())
print("Promedio de edad:", df['Age'].mean())
menores_18 = df[df['Age'] < 18]
print("\nPersonas menores de 18 años:\n", menores_18)
