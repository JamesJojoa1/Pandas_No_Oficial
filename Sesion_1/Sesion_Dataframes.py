#Importamos la biblioteca pandas y la llamamos 'pd'
import pandas as pd

# Creamos un serie de pandas que es como un lista con etiquetas
# Los valores son nombres de jugadores de PSG
# El índice especifica los números de camiseta de esos jugadores
psg_players = pd.Series(
    ['Navas', 'Mbappe', 'Neymar', 'Messi'], # lista de jugadores
    index=[1, 7, 10, 30]                    # Lista de índices (números de camisetas)
)
# Creamos un serie de pandas usando una lista
psg_players_list = pd.Series(
    ['Navas', 'Mbappe', 'Neymar', 'Messi'], # lista de jugadores
)
# Creamos un diccionario que asocie números de camisetas con nombres de jugadores
psg_dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'}

# Creamos una serie de pandas usando el diccionario
psg_players_dict = pd.Series(psg_dict)

# Imprimimos la serie creada a partir del diccionario
print(psg_players_dict)

# Imprimimos el valor en la posición (índices) 7 de la Serie creada a partir del diccionario
print(psg_players_dict[7])
print(psg_players_dict[0:3])

# Diccionario con datos de jugadores
dict = {'Jugador': ['Navas', 'Mbappe', 'Neymar', 'Messi'],
        'Altura': [183.0, 170.0, 170.0, 165.0],
        'Goles': [2, 200, 150, 200]}

# Creamos un DataFrame con el diccionario de índices personalizados
df = pd.DataFrame(dict, index=[1, 7, 10, 30])

# Imprimimos el DataFrame
print(df)