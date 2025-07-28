import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Fase1_Data_Scientist_Junior/Modulo2_numpypandas/train.csv")
sns.set(style="whitegrid")  # Mejora el aspecto de todos los gráficos


# Histogramas

plt.figure(figsize=(8, 4))
sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title('Distribución de edades')
plt.xlabel('Edad')
plt.ylabel('Cantidad')
plt.show()

# Boxplot (comparación por grupo)

plt.figure(figsize=(8, 4))
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Edad por supervivencia')
plt.xlabel('¿Sobrevivió? (0=No, 1=Sí)')
plt.ylabel('Edad')
plt.show()

# Gráficos de barras / Countplot

plt.figure(figsize=(6, 4))
sns.countplot(x='Pclass', data=df)
plt.title('Cantidad de pasajeros por clase')
plt.xlabel('Clase')
plt.ylabel('Cantidad')
plt.show()

# Barplot con media (comparación estadística)

plt.figure(figsize=(8, 4))
sns.barplot(x='Pclass', y='Fare', data=df, errorbar=None)
plt.title('Tarifa promedio por clase')
plt.xlabel('Clase')
plt.ylabel('Tarifa promedio')
plt.show()

# Scatterplot (relación entre dos variables continuas)

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title('Edad vs Tarifa, coloreado por supervivencia')
plt.xlabel('Edad')
plt.ylabel('Tarifa')
plt.legend(title='¿Sobrevivió?')
plt.show()

# Heatmap (matriz de correlación)

plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title('Matriz de correlación')
plt.show()
