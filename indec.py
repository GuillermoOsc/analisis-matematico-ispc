import pandas as pd
import requests
import zipfile
from io import BytesIO

# URL del ZIP con CSV del INDEC
url = "https://www.indec.gob.ar/ftp/cuadros/menusuperior/enpd/base_estudio_discapacidad_2018.zip"

# Descargar el archivo ZIP
response = requests.get(url)
if response.status_code != 200:
    print(f"Error al descargar: {response.status_code}")
    exit()

# Extraer el contenido del ZIP
with zipfile.ZipFile(BytesIO(response.content)) as zip_file:
    # Buscar archivos .csv dentro del ZIP
    csv_files = [f for f in zip_file.namelist() if f.endswith('.csv')]

    if not csv_files:
        print("❌ No se encontró ningún archivo CSV en el ZIP.")
        exit()

    # Mostrar archivos encontrados
    print(f"✅ Archivos CSV encontrados: {csv_files}")

    # Leer el primer CSV
    with zip_file.open(csv_files[0]) as file:
        df = pd.read_csv(file, encoding='latin1')  # Cambiar a 'utf-8' si es necesario

# Mostrar info del DataFrame
print("\n✅ Primeras filas del DataFrame:")
print(df.head())

print("\n📋 Columnas:")
print(df.columns.tolist())

print(f"\n📏 Dimensiones del DataFrame: {df.shape}")
