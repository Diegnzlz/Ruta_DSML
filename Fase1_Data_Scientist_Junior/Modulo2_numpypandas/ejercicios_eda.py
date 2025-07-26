import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Fase1_Data_Scientist_Junior/Modulo2_numpypandas/train.csv")

# Ejercicios prácticos
# Cuenta cuántos valores nulos hay en cada columna.
print("cuantos valores nulos hay por columna:")
print(df.isnull().sum())


# Calcula el promedio de edad de los sobrevivientes vs no sobrevivientes.
print("Promedio de edad de sobrevivientes vs no sobrevivientes:")
print(df.groupby('Survived')['Age'].mean())

# ¿Cuántos pasajeros embarcaron en cada puerto (“Embarked”)?
print("Cuantos pasajeros embarcaron en cada puerto:")
print(df['Embarked'].value_counts())

# ¿Qué porcentaje de pasajeros eran mujeres?
print("que porcentaje de pasajeros eran mujeres:")
total = len(df)
porcentaje = (df['Sex'].value_counts()["female"] / total) * 100

print(f"Porcentaje de pasajeras: {porcentaje:.2f}%")

# Encuentra el rango de edades (mínimo y máximo).
print("rango de edades:")
rango_edades = df['Age'].agg(['min', 'max'])
print(rango_edades)

# Haz un gráfico de barras de la cantidad de pasajeros por clase (“Pclass”).
df['Pclass'].hist(bins=20)
plt.title("Cantidad de pasajeros por clase")
plt.xlabel("Clase")
plt.ylabel("Cantidad")
plt.show()

# Encuentra la correlación entre “Fare” (tarifa) y “Survived”.
print("correlacion entre el pago de tarifa y la cantidad de sobrevivientes")
correlacion = df["Fare"].corr(df["Survived"])
print("Correlación entre Fare y Survived:", correlacion)
