import matplotlib.pyplot as plt
import pandas as pd

# Cargar dataset (ajusta el path si usas Colab o local)
df = pd.read_csv("Fase1_Data_Scientist_Junior/Modulo2_numpypandas/train.csv")

# Ver las primeras filas
print(df.head())

# Información general y tipos de datos
print(df.info())

# Estadísticas básicas
print(df.describe())

# Valores únicos de una columna (ejemplo: Sex)
print(df['Sex'].value_counts())

# Nulos por columna
print(df.isnull().sum())

# Eliminar filas duplicadas (si hay)
df = df.drop_duplicates()

# ¿Cuántos sobrevivieron?
print(df['Survived'].value_counts())

# Agrupaciones: promedio de edad por sexo
print(df.groupby('Sex')['Age'].mean())

# Correlación entre variables numéricas
print(df.corr(numeric_only=True))

# Visualización simple: histograma de edades
df['Age'].hist(bins=20)
plt.title("Distribución de edades")
plt.xlabel("Edad")
plt.ylabel("Cantidad")
plt.show()
