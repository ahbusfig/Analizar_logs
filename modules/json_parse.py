import json
import pandas as pd

def parse_json(filepath):
    try:
        # Cargar el JSON desde el archivo
        with open(filepath, "r") as file:
            log_data = json.load(file)

        # Convertir a DataFrame
        df = pd.DataFrame(log_data)
    except FileNotFoundError:
        print(f"Error: El archivo {filepath} no fue encontrado.")
        return
    except json.JSONDecodeError:
        print("Error: No se pudo decodificar el archivo JSON.")
        return
    except Exception as e:
        print(f"Error inesperado: {e}")
        return

    # Mostrar el DataFrame
    return df
