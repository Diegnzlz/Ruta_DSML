from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

df = pd.read_csv("Fase1_Data_Scientist_Junior/Modulo2_numpypandas/train.csv")

# 1. Detección de nulos
print(df.isnull().sum())

# 2. Relleno de nulos
# Ejemplo: Rellenar 'Age' con la mediana
df['Age'] = df['Age'].fillna(df['Age'].median())

# 'Embarked': solo tiene 2 nulos, rellenar con la moda (valor más frecuente)
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# 'Fare': solo tiene 1 nulo, rellenar con la mediana
df['Fare'] = df['Fare'].fillna(df['Fare'].median())

# 3. Eliminación de columnas poco útiles o con demasiados nulos
df = df.drop(['Cabin', 'Ticket', 'Name'], axis=1)

# 4. Codificación de variables categóricas (sexo y puerto)
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# 5. Eliminación de duplicados
df = df.drop_duplicates()

# 6. Escalado (opcional, para modelos ML)
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
