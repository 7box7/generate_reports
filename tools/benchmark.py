import time
import csv
from reports import median_coffee_report
from typing import List, Dict

def read_csv(file_path: str) -> List[Dict[str, str]]:
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data


data = read_csv('big_data.csv')

start = time.time()
result_bisect = median_coffee_report(data)
time_bisect = time.time() - start
print(f"Bisect версия: {time_bisect:.4f} секунд")
