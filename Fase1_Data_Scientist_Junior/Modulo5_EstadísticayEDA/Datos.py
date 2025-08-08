import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Configuración inicial
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# Carga de datos
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["MedHouseVal"] = data.target

# 1. Análisis estadístico básico
print("="*50)
print("Primeras filas del dataset:")
print(df.head())

print("\n" + "="*50)
print("Estadísticas descriptivas:")
print(df.describe())

print("\n" + "="*50)
print("Mediana de las variables:")
print(df.median(numeric_only=True))

print("\n" + "="*50)
print("Moda de las variables:")
print(df.mode().iloc[0])

print("\n" + "="*50)
print("Desviación estándar:")
print(df.std(numeric_only=True))

# 2. Visualización de distribuciones
plt.figure(figsize=(12, 8))
for i, col in enumerate(df.columns[:-1]):  # Excluyendo MedHouseVal
    plt.subplot(3, 3, i+1)
    sns.histplot(df[col], bins=30, kde=True)
    plt.title(f'Distribución de {col}')
plt.tight_layout()
plt.show()

# 3. Boxplots
plt.figure(figsize=(12, 8))
for i, col in enumerate(df.columns[:-1]):
    plt.subplot(3, 3, i+1)
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot de {col}')
plt.tight_layout()
plt.show()

# 4. Análisis de correlación
corr = df.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f",
            annot_kws={"size": 10}, vmin=-1, vmax=1)
plt.title('Matriz de Correlación', pad=20)
plt.tight_layout()
plt.show()

# 5. Relación entre variables y el target
plt.figure(figsize=(12, 8))
for i, col in enumerate(df.columns[:-1]):
    plt.subplot(3, 3, i+1)
    sns.scatterplot(x=df[col], y=df['MedHouseVal'], alpha=0.5)
    plt.title(f'{col} vs Valor de la Casa')
plt.tight_layout()
plt.show()
