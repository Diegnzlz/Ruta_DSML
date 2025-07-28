1. Principales tareas de preprocesamiento
1️⃣ Detección y tratamiento de valores nulos
.isnull().sum() — Cuenta nulos por columna.

.dropna() — Elimina filas o columnas con nulos.

.fillna(valor) — Rellena nulos con un valor, media, mediana, moda, etc.

2️⃣ Detección y tratamiento de outliers
Boxplots y estadísticas (.describe()) ayudan a encontrar valores atípicos.

Puedes eliminar o reemplazar outliers según el contexto.

3️⃣ Conversión de tipos de datos
Cambia tipos con .astype() (por ejemplo, object a int o float).

Convierte fechas con pd.to_datetime().

4️⃣ Codificación de variables categóricas
Label Encoding: Cambia texto por números (para variables ordinales).

One-Hot Encoding: Usa columnas binarias para cada categoría (para variables nominales).

Se hace con pd.get_dummies() o sklearn.preprocessing.OneHotEncoder.

5️⃣ Escalado y normalización
Hace que los valores de las columnas numéricas estén en la misma escala.

Usar: StandardScaler, MinMaxScaler de sklearn.preprocessing.

6️⃣ Eliminación de duplicados
.duplicated() y .drop_duplicates().
