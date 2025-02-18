# Log Analyzer

**Log Analyzer** es una herramienta de análisis de logs diseñada para procesar y estructurar datos de diferentes formatos de registro, incluidos Apache, CSV, JSON y Syslog. Es ideal para administradores de sistemas y analistas de seguridad que necesitan gestionar y analizar registros de manera eficiente.

---

## 🔧 **Funcionalidades**

- Procesar y extraer datos clave de logs de Apache.
- Analizar registros en formato CSV.
- Cargar y convertir logs JSON a DataFrames.
- Procesar logs Syslog con información de procesos y mensajes.
- Manejo de errores para archivos inexistentes o formatos incorrectos.

---

## 📦 **Requisitos**

Las dependencias necesarias están listadas en `requirements.txt`. Instálalas ejecutando:

```bash
pip install -r requirements.txt
```

### Dependencias principales:

- `pandas`: Manejo y análisis de datos.
- `termcolor`: Para resaltar mensajes en la consola.

---

## 🚀 **Instrucciones de uso**

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/log-analyzer.git
   cd log-analyzer
   ```

2. Ejecuta el script principal:

   ```bash
   python main.py <nombre_del_archivo>
   ```

   Asegúrate de colocar el archivo de log en la carpeta `sample_logs`.

3. Ejemplo de ejecución:

   ```bash
   python main.py apache_log.txt
   ```

---

## 🐂 **Estructura del proyecto**

```plaintext
ANALIZAR_LOGS/
│
├── modules/               # Módulos de procesamiento de logs
│   ├── apache_log.py      # Parser de logs de Apache
│   ├── csv_log.py         # Parser de logs CSV
│   ├── json_parse.py      # Parser de logs JSON
│   └── sys_log.py         # Parser de logs Syslog
│
├── sample_logs/           # Carpeta con logs de muestra
├── main.py                # Script principal
├── parser.py              # Orquestador de parsers
└── requirements.txt       # Dependencias del proyecto
```
