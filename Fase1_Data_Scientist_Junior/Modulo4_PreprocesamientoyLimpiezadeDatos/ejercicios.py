from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Fase1_Data_Scientist_Junior/Modulo2_numpypandas/train.csv")

print(df.describe())

plt.figure(figsize=(6, 3))
plt.title('Boxplot de Fare antes de limpiar')
plt.boxplot(df['Fare'].dropna())
plt.ylabel('Fare')
plt.show()

# 1) Identifica y trata los valores nulos de tu dataset.
print(df.isnull().sum())

# Elimina columnas que no aportan información relevante o que tienen demasiados nulos.
df = df.drop(['Cabin', 'Ticket'], axis=1)

# Codifica las variables categóricas.
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# Elimina duplicados.
df = df.drop_duplicates()

# Escala las variables numéricas Age y Fare usando StandardScaler o MinMaxScaler.
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Fare'] = df['Fare'].fillna(df['Fare'].median())

# (Opcional) Realiza un boxplot antes y después de limpiar outliers en Fare.

print(df.describe())

q99 = df['Fare'].quantile(0.99)
df['Fare'] = np.where(df['Fare'] > q99, q99, df['Fare'])

# Boxplot de 'Fare' DESPUÉS de limpiar outliers
plt.figure(figsize=(6, 3))
plt.title('Boxplot de Fare después de limpiar')
plt.boxplot(df['Fare'].dropna())
plt.ylabel('Fare')
plt.show()
