import re
import pandas as pd

# Patrón para analizar los registros de syslog
pattern = r'^(\w{3} \d+ \d{2}:\d{2}:\d{2}) ([\w.-]+) (\w+)\[(\d+)\]: (.+)$'
#Feb 10 14:26:30 server1 systemd[1]: Stopping Apache HTTP Server...
def parse_syslog(filepath):
    data = []
    
    with open(filepath, "r") as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                timestamp, host, process, pid, message = match.groups()
                data.append([timestamp, host, process, pid, message])
    
    return pd.DataFrame(data, columns=["Timestamp", "Host", "Process", "PID", "Message"])



