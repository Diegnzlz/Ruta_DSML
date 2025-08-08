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

# 1. Análisis de otras variables importantes
plt.figure(figsize=(10, 5))
sns.histplot(df['HouseAge'], bins=30, kde=True)
plt.title('Distribución de Antigüedad de Viviendas (HouseAge)')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(x=df['AveRooms'])
plt.title('Boxplot de Habitaciones Promedio (AveRooms)')
plt.show()

# 2. Identificar outliers y asimetrías

# Estadísticas clave para detectar outliers
print(df[['HouseAge', 'AveRooms', 'Population', 'AveOccup']].describe())

# Boxplot comparativo
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['HouseAge', 'AveRooms', 'Population', 'AveOccup']])
plt.title('Comparación de Variables')
plt.show()

# 3. Analizar correlaciones

# Matriz de correlación
corr = df.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación')
plt.show()

# Scatterplot para variables correlacionadas
sns.scatterplot(x='MedInc', y='MedHouseVal', data=df, alpha=0.5)
plt.title('Relación entre Ingreso Medio y Valor de la Vivienda')
plt.show()

# EXTRA
# Gráfico de dispersión con ajuste lineal
sns.lmplot(x='MedInc', y='MedHouseVal', data=df, height=6, aspect=1.5)
plt.title('Relación lineal entre Ingreso y Valor de Vivienda')
plt.show()
