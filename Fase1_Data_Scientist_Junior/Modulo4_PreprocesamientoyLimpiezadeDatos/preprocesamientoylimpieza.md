# Preprocesamiento y limpieza de datos: Titanic

---

## 1. Carga y análisis inicial del dataset

````python
import pandas as pd
df = pd.read_csv("Fase1_Data_Scientist_Junior/Modulo2_numpypandas/train.csv")
print(df.describe())
print(df.isnull().sum())
````

Analizamos los valores nulos y las estadísticas principales de cada columna.

---

## 2. Tratamiento de valores nulos

* Age y Fare presentan valores nulos.

* Llenamos los nulos con la mediana, que es robusta frente a outliers.

````python

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Fare'] = df['Fare'].fillna(df['Fare'].median())
````

---

### 3. Eliminación de columnas irrelevantes

Eliminamos las columnas 'Cabin' y 'Ticket' porque tienen demasiados valores nulos o no aportan valor para el análisis/modelado inicial.

````python
df = df.drop(['Cabin', 'Ticket'], axis=1)
````

---

## 4. Codificación de variables categóricas

Codificamos las variables 'Sex' y 'Embarked' usando One-Hot Encoding para facilitar su uso en modelos de machine learning.

````python
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
````

---

## 5. Eliminación de duplicados

Eliminamos filas duplicadas para evitar sesgos en el análisis/modelado.

````python
df = df.drop_duplicates()
````

---

## 6. Escalado de variables numéricas

Escalamos 'Age' y 'Fare' usando StandardScaler para que tengan media 0 y desviación estándar 1.

````python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
````

---

## 7. Análisis de outliers en 'Fare'

Mostramos boxplots de 'Fare' antes y después de limpiar outliers (recortando valores extremos por encima del percentil 99).

````python
import matplotlib.pyplot as plt
import numpy as np

# Boxplot de 'Fare' antes de limpiar outliers
plt.figure(figsize=(6, 3))
plt.title('Boxplot de Fare antes de limpiar')
plt.boxplot(df['Fare'].dropna())
plt.ylabel('Fare')
plt.show()

# Recorte de outliers en 'Fare'
q99 = df['Fare'].quantile(0.99)
df['Fare'] = np.where(df['Fare'] > q99, q99, df['Fare'])

# Boxplot de 'Fare' después de limpiar outliers
plt.figure(figsize=(6, 3))
plt.title('Boxplot de Fare después de limpiar')
plt.boxplot(df['Fare'].dropna())
plt.ylabel('Fare')
plt.show()

````

---

## 8. Conclusiones

* Se trataron los valores nulos en 'Age' y 'Fare' usando la mediana.

* Se eliminaron columnas poco útiles ('Cabin', 'Ticket').

* Se codificaron variables categóricas y se eliminaron duplicados.

* Se escalaron las variables numéricas para facilitar el modelado.

* Se realizó un análisis visual de outliers en 'Fare'.

El dataset está ahora listo para análisis avanzados y para ser usado en modelos de Machine Learning.

Autor: Diego González — Preprocesamiento Titanic 2025
