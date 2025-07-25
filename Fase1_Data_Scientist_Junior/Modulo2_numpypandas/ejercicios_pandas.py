# Pandas:
import pandas as pd
# Crea un DataFrame con 5 amigos, sus edades y ciudades.

data = {
    'Nombre': ['Diego', 'Ana', 'Luis', 'Maria', 'Pedro'],
    'Ciudad': ['Valencia', 'Caracas', 'Maracay', 'Caracas', 'Maracay'],
    'Edad': [20, 30, 45, 18, 8]
}
df = pd.DataFrame(data)
# Filtra los que viven en "Caracas" y son mayores de 20 años.
print("Filtrar Caracas y mayor de 20 años:")
Ccs = df[df['Ciudad'] == "Caracas"]
Mayores = Ccs[Ccs['Edad'] > 25]
print(Mayores)

# Agrega una columna que diga "mayor_de_edad" (True o False).
df['Mayor'] = df['Edad'] >= 18
print(df)
