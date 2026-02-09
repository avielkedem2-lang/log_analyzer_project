import csv
from pathlib import Path
PATH_LOG = Path("network_traffic.log")
def list_fields(file_csv):
    try:
        with open(file_csv, "r") as f:
            return list(csv.reader(f))
    except Exception as fild:
        print(fild)
