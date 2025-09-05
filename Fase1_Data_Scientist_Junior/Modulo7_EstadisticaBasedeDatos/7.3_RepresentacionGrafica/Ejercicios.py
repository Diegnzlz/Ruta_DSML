import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Cargar dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

# Histograma de la variable MedHouseVal
sns.histplot(data=df, x="MedHouseVal", bins=30, kde=True)
plt.title("Distribución de la valor de las casas")

plt.show()

# boxplot de AveRooms
sns.boxplot(data=df, y="AveRooms")
plt.title("Boxplot de la cantidad de habitaciones")
plt.show()

# scatterplot entre AveOccup y MedHouseVal

sns.scatterplot(data=df, x="AveOccup", y="MedHouseVal")
plt.title("Relación entre Edad de Vivienda y numero de ocupantes")
plt.show()
