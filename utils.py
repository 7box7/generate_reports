import csv
import sys
from typing import List, Dict, Optional

def read_csv_files(file_paths: List[str], headers: Optional[List[str]] = None) -> List[Dict[str, str]]:
    data = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header_row = next(reader)
                if headers:
                    indices = [header_row.index(h) for h in headers if h in header_row]
                    for row in reader:
                        if len(row) > max(indices):
                            data.append({headers[i]: row[idx] for i, idx in enumerate(indices)})
                else:
                    f.seek(0)
                    dict_reader = csv.DictReader(f)
                    data.extend(list(dict_reader))
        except FileNotFoundError:
            print(f"Ошибка: файл {file_path} не найден.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Ошибка чтения файла {file_path}: {e}", file=sys.stderr)
            sys.exit(1)
    return data
