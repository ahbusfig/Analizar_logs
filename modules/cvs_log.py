import re
import pandas as pd
from termcolor import colored

def parse_csv(filepath):
    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}),(\d+\.\d+\.\d+\.\d+),(.+?),(\d+),(\d+)"
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

    return pd.DataFrame(data, columns=["date", "timestamp", "ip", "request", "status", "size"])


