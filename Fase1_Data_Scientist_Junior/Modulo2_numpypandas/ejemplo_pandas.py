import pandas as pd

# Crear un DataFrame desde un diccionario
data = {
    "nombre": ["Ana", "Beto", "Clara"],
    "edad": [21, 17, 34],
    "ciudad": ["Caracas", "Maracay", "Valencia"]
}
df = pd.DataFrame(data)
print(df)

# Leer un archivo CSV (descárgalo o usa uno propio)
# df = pd.read_csv("archivo.csv")

# Acceso rápido
print("Nombres:", df["nombre"])
print("Primer registro:\n", df.iloc[0])

# Filtrar filas: mayores de 18
mayores = df[df["edad"] > 18]
print("Mayores de 18:\n", mayores)
