import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Fase1_Data_Scientist_Junior/Modulo2_numpypandas/train.csv")
# Mejora el aspecto de todos los gráficos
sns.set_theme(style="darkgrid", palette="viridis")


# Ejercicios para ti
# Haz un histograma de la tarifa (“Fare”) con Seaborn.
plt.figure(figsize=(8, 4))
sns.histplot(df['Fare'].dropna(), bins=20, kde=True)
plt.title('Distribución de Tarifas')
plt.xlabel('Tarifa')
plt.ylabel('Cantidad')
plt.show()

# Crea un boxplot de edad por clase (“Pclass”).
plt.figure(figsize=(8, 4))
sns.boxplot(x='Pclass', y='Age', data=df)
plt.title('Edad por clase')
plt.xlabel('Clase 1 2 3')
plt.ylabel('Edad')
plt.show()

# Haz un countplot de pasajeros por sexo (“Sex”).

plt.figure(figsize=(6, 4))
sns.countplot(x='Sex', data=df)
plt.title('Cantidad de pasajeros por sexo')
plt.xlabel('Sexo')
plt.ylabel('Cantidad')
plt.show()

# Muestra un barplot de supervivientes por clase (“Pclass”).
plt.figure(figsize=(8, 4))
sns.barplot(x='Pclass', y='Survived', data=df, errorbar=None)
plt.title('promedio de sobrevivientes por clase')
plt.xlabel('Clase')
plt.ylabel('Sobrevivientes')
plt.show()

# Genera un heatmap de correlaciones solo para las columnas numéricas.

plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title('Matriz de correlación')
plt.show()
