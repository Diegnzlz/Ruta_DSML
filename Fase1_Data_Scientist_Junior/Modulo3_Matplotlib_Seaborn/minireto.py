import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Fase1_Data_Scientist_Junior/Modulo2_numpypandas/train.csv")
sns.set_theme(style="darkgrid", palette="viridis")

# Mini-reto

# Elige dos variables que te llamen la atención
# (ejemplo: “SibSp” y “Survived”, o “Age” y “Fare”),
#  haz un gráfico que muestre la relación, y saca una pequeña conclusión de lo que ves.

# 1. Tabla de cantidad de mujeres y hombres por clase social
print("Cantidad de mujeres y hombres por clase social:")
tabla_sexo_clase = pd.crosstab(df['Pclass'], df['Sex'])
print(tabla_sexo_clase)

# 2. Gráfico: Distribución de sexo por clase
plt.figure(figsize=(7, 5))
sns.countplot(x='Pclass', hue='Sex', data=df)
plt.title('Cantidad de mujeres y hombres por clase')
plt.xlabel('Clase')
plt.ylabel('Cantidad')
plt.legend(title='Sexo')
plt.tight_layout()
plt.savefig("sexo_por_clase.png")
plt.show()

# 3. Tabla: Sobrevivientes por clase y sexo (conteo)
print("\nTabla de sobrevivientes por clase y sexo (conteo):")
tabla_surv = pd.crosstab([df['Pclass'], df['Sex']], df['Survived'])
print(tabla_surv)

# 4. Gráficos: Sobrevivientes por clase y sexo
# Mujeres
plt.figure(figsize=(7, 5))
sns.countplot(x='Pclass', hue='Survived', data=df[df['Sex'] == 'female'])
plt.title('Supervivientes mujeres por clase')
plt.xlabel('Clase')
plt.ylabel('Cantidad')
plt.legend(title='¿Sobrevivió?', labels=['No', 'Sí'])
plt.tight_layout()
plt.savefig("supervivientes_mujeres_por_clase.png")
plt.show()

# Hombres
plt.figure(figsize=(7, 5))
sns.countplot(x='Pclass', hue='Survived', data=df[df['Sex'] == 'male'])
plt.title('Supervivientes hombres por clase')
plt.xlabel('Clase')
plt.ylabel('Cantidad')
plt.legend(title='¿Sobrevivió?', labels=['No', 'Sí'])
plt.tight_layout()
plt.savefig("supervivientes_hombres_por_clase.png")
plt.show()

# 5. Porcentaje de supervivencia por clase y sexo
print("\nPorcentaje de supervivencia por clase y sexo:")
porc_surv = df.groupby(['Pclass', 'Sex'])['Survived'].mean().unstack()
print(porc_surv)

# 6. Gráfico de porcentaje de supervivencia (opcional)
porc_surv.plot(kind='bar', figsize=(8, 6))
plt.title('Tasa de supervivencia por clase y sexo')
plt.ylabel('Porcentaje de supervivencia')
plt.xlabel('Clase')
plt.legend(title='Sexo')
plt.tight_layout()
plt.savefig("tasa_supervivencia_por_clase_y_sexo.png")
plt.show()
