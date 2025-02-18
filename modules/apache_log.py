import pandas as pd
import re
from termcolor import colored

def parse_apache(filepath):

    # Ejemplo pattern --> 192.168.0.2 - - [04/Feb/2025:10:06:47 -0500] "POST /login HTTP/1.1" 404 567
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+|-)'
    data = []

    try:
        with open(filepath, "r") as file:
            for line in file:
                match = re.match(pattern, line)
                if match:
                    data.append(match.groups())
    except FileNotFoundError:
        print(f"Error: El archivo '{filepath}' no existe.")
        return pd.DataFrame()

    return pd.DataFrame(data, columns=["IP", "Timestamp", "Request", "Status", "Size"])

