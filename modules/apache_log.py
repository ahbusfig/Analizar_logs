import pandas as pd
import re
from termcolor import colored

def parse_apache(filepath):
    """
    The regular expression pattern used for parsing log lines is:
        r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+|-)'
        - (\d+\.\d+\.\d+\.\d+): Matches the IP address.
        - - -: Matches the literal characters " - - ".
        - \[(.*?)\]: Matches the timestamp enclosed in square brackets.
        - "(.*?)": Matches the request line enclosed in double quotes.
        - (\d+): Matches the status code.
        - (\d+|-) : Matches the size of the response in bytes or a dash if the size is not available.
    """
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

