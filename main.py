import argparse
import os
from parser import procesar_log

# Obtener el directorio actual
ruta_actual = os.getcwd()

def main():
    # Configurar argparse
    parser_arg = argparse.ArgumentParser(description="Parser de logs para diferentes formatos")
    parser_arg.add_argument("filename", type=str, help="Nombre del archivo de log a procesar(dentro de la carpeta sample_logs)")
    
    # Parsear argumentos
    args = parser_arg.parse_args()

    # Combinar la ruta del directorio actual con la carpeta 'sample_logs' y el nombre del archivo
    ruta_completa = os.path.join(ruta_actual, "sample_logs", args.filename)

    # Normalizar la ruta para asegurar compatibilidad en Windows
    ruta_normalizada = os.path.normpath(ruta_completa)

    # Imprimir la ruta con doble barra para depuración
    print(f"\nProcesando archivo: {ruta_normalizada}\n")

    # Procesar el log
    procesar_log(ruta_normalizada)


if __name__ == "__main__":
    main()
