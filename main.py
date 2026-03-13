import argparse
import sys
from tabulate import tabulate
from reports import *
from utils import read_csv_files
from typing import Dict, List, Callable, Any

REPORTS: Dict[str, Callable[[List[Dict[str, str]]], List[Tuple[str, float]]]] = {
    'median-coffee': median_coffee_report,
}

REQUIRED_FIELDS: Dict[str, List[str]] = {
    'median-coffee': ['student', 'coffee_spent']
}

HEADERS: Dict[str, List[str]] = {
    'median-coffee': ['student', 'median_coffee']
}

def main() -> None:
    parser = argparse.ArgumentParser(description="Генерация отчета")
    parser.add_argument('--files', nargs='+', required=True, help="CSV файлы для обработки")
    parser.add_argument('--report', required=True, help="Тип отчета")

    args = parser.parse_args()

    if args.report in REPORTS:
        data = read_csv_files(args.files, headers=REQUIRED_FIELDS[args.report])
        report_data = REPORTS[args.report](data)
        headers = HEADERS[args.report]
        print(tabulate(report_data, headers=headers, tablefmt='grid'))
    else:
        print(f"Ошибка: неизвестный отчет '{args.report}'", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
