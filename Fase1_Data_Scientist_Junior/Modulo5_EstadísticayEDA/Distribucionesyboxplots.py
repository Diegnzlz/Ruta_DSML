import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)  # type: ignore
df["MedHouseVal"] = data.target  # type: ignore
print(df.head())

plt.figure(figsize=(8, 4))
sns.histplot(df['MedInc'], bins=30, kde=True)
plt.title('Distribución de ingreso medio (MedInc)')
plt.show()

plt.figure(figsize=(8, 4))
sns.boxplot(x=df['MedInc'])
plt.title('Boxplot de ingreso medio (MedInc)')
plt.show()

corr = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title('Matriz de correlación')
plt.show()
