# Mini-reto
# Descarga o crea un archivo CSV con nombres, edades y notas de estudiantes.
# Carga el archivo con Pandas.
# Calcula el promedio de notas.
# Crea una columna "aprobado" (nota >= 10).
# Guarda el nuevo DataFrame como "resultados.csv".
import pandas as pd

df = pd.read_csv(
    "Fase1_Data_Scientist_Junior/Modulo2_numpypandas/personas.csv")
print("Promedio de notas:", df['nota'].mean())

df['aprobado'] = df['nota'] >= 10
df.to_csv('Fase1_Data_Scientist_Junior/Modulo2_numpypandas/resultados.csv',
          index=False, encoding='utf-8')
print(df)
