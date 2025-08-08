import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)  # type: ignore
df["MedHouseVal"] = data.target  # type: ignore
print(df.head())


print(df.describe())
print("Mediana:\n", df.median())
print("Moda:\n", df.mode().iloc[0])
print("Desviación estándar:\n", df.std())
