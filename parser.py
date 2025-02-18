import os
import re
from modules.cvs_log import parse_csv
from modules.json_parse import parse_json
from modules.apache_log import parse_apache
from modules.sys_log import parse_syslog

def detectar_formato(filepath):
    """
    Detecta el formato del log basado en su extensión y contenido.
    - CSV -> .csv
    - JSON -> .json
    - Apache -> .log con estructura de Apache
    - Syslog -> .log con estructura de Syslog
    """
    # Obtén la extensión del archivo
    ext = os.path.splitext(filepath)[1].lower()

    # Detección basada en la extensión
    if ext == ".csv":
        return "csv"
    elif ext == ".json":
        return "json"
    elif ext in [".log", ".txt"]:
        # Intentar leer el contenido del archivo para verificar el formato
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                first_line = f.readline().strip()
        except Exception as e:
            print(f"Error al abrir el archivo '{filepath}': {e}")
            return None

        # Patrón para Apache (IP + fecha entre corchetes)
        apache_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - - \[\d{2}/[A-Za-z]+/\d{4}:'
        # Patrón para Syslog (mes día hora máquina servicio)
        syslog_pattern = r'^[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}'

        if re.match(apache_pattern, first_line):
            return "apache"
        elif re.match(syslog_pattern, first_line):
            return "syslog"
        else:
            print("Formato de log desconocido o archivo vacío.")
            return None

    # Si no coincide con ningún formato conocido
    print(f"Extensión de archivo desconocida: {ext}")
    return None

def procesar_log(filepath):
    """
    Procesa el log según el formato detectado.
    Llama al parser correspondiente (CSV, JSON, Apache, Syslog).
    """
    formato = detectar_formato(filepath)

    # Diccionario de parsers
    parsers = {
        "csv": parse_csv,
        "json": parse_json,
        "apache": parse_apache,
        "syslog": parse_syslog,
    }

    # Llamar al parser correspondiente
    if formato in parsers:
        try:
            return print(parsers[formato](filepath))
        except Exception as e:
            print(f"Error al procesar el archivo '{filepath}': {e}")
            return None
    else:
        print("Formato desconocido o no soportado.")
        return None
