# Importa la libreria Pandas, que es fundamental para le análisis de datos.
import pandas as pd

# Define la ruta del archivo CSV que contiene los datos.
# Si el archivo esta en el mismo directorio que el script, basta con poner el nombre del archivo.
path = 'RickAndMortyScripts.csv'

# lee el archivo CSV usando la función 'read_csv' de Pandas.
# Se especifica la codificación 'latin1' (también conocida como ISO-8859-1) para mejorar caracteres especiales.
retail_data = pd.read_csv(path, encoding='latin1')

# Muestra el tipo de variable 'retail_data' para confirmar que es un DataFrame.
# Un DataFrame es una estructura de datos bidimensionales (filas y columnas) similar a una tabla.
print(type(retail_data))

# Imprime todo el contenido del DataFrame 'retail_data' para visualizar los datos que fueron leídos del archivo CSV.
print(retail_data)