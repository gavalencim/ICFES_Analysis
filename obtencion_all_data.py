# ESTE ES EL QUE FUNCIONA!!!

import requests
import pandas as pd
import time

BASE_URL = "https://www.datos.gov.co/resource/kgxf-xxbe.json" # URL de la API

CHUNK_SIZE = 50000 # Número de registros por solicitud
TOTAL_ROWS = 7109704 # Límite de registros

# Crear carpeta para guardar el CSV si no existe
## os.makedirs("datafull", exist_ok=True)

output_file = "icfes_full_data.csv" # Nombre del archivo final

# Bandera para controlar si ya escribimos el encabezado
header_written = False

# Apertura del archivo final una sola vez en modo append
with open(output_file, "w", encoding="utf-8", newline="") as f_out:
    # Recorrido de los datos por bloques de tamano chunk
    for offset in range(0, TOTAL_ROWS, CHUNK_SIZE):
        print(f"📦 Descargando registros desde {offset} hasta {offset + CHUNK_SIZE}...") # Visibilización de ejecución

        # Parámetros de la solicitud GET
        params = {
            "$limit": CHUNK_SIZE,
            "$offset": offset
        }

        # Solicitud GET
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            chunk = response.json() # Paso de la respuesta de la API a formato Json

            if not chunk:
                print("✅ No hay más datos que descargar.")
                break # Si no hay más datos sale del ciclo

            df_chunk = pd.DataFrame(chunk) # Paso del formato Json a un dataframe

            df_chunk.to_csv(f_out, index=False, header=not header_written) # Guardado directamente en el CSV
            header_written = True  # Después de la primera vez, no se escriben más encabezados

            # Pausa opcional para no sobrecargar la API
            time.sleep(1)
        else:
            print(f"❌ Error en offset {offset}: {response.status_code}")
            break

print("🎉 Descarga completa. Archivo guardado en:", output_file)
