import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Cargar dataset
data = fetch_california_housing(as_frame=True)
df = data.frame
# Histograma de la variable HouseAge
sns.histplot(data=df, x="HouseAge", bins=30, kde=True)
plt.title("Distribución de la Edad de las Viviendas")
plt.show()
# Boxplot
sns.boxplot(data=df, y="HouseAge")
plt.title("Boxplot de la Edad de las Viviendas")
plt.show()
# Scatterplot
sns.scatterplot(data=df, x="HouseAge", y="MedHouseVal")
plt.title("Relación entre Edad de Vivienda y Valor Medio")
plt.show()
