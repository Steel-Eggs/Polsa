#!/usr/bin/env python3
"""Convert finance/expenses_*.csv files into finance/expenses-data.js for the dashboard."""

from __future__ import annotations

import csv
import json
from decimal import Decimal
from pathlib import Path

FINANCE_DIR = Path('finance')
OUTPUT_JSON = FINANCE_DIR / 'expenses-data.json'
OUTPUT_JS = FINANCE_DIR / 'expenses-data.js'
DASHBOARD_JS = FINANCE_DIR / 'dashboard' / 'expenses-data.js'


def read_csv(file_path: Path) -> list[dict]:
    rows: list[dict] = []
    with file_path.open(encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            clean: dict = {}
            for key, value in row.items():
                if isinstance(value, str):
                    value = value.strip()
                clean[key] = value
            for numeric_field in ('quantity', 'unit_price_rub', 'line_total_rub'):
                val = clean.get(numeric_field)
                if val in (None, ''):
                    clean[numeric_field] = None
                else:
                    clean[numeric_field] = float(round(Decimal(val), 2))
            rows.append(clean)
    return rows


def main() -> None:
    csv_files = sorted(FINANCE_DIR.glob('expenses_*.csv'))
    if not csv_files:
        raise SystemExit('Нет файлов expenses_*.csv')

    combined: list[dict] = []
    for csv_file in csv_files:
        combined.extend(read_csv(csv_file))

    OUTPUT_JSON.write_text(json.dumps(combined, ensure_ascii=False, indent=2), encoding='utf-8')
    js_payload = 'window.EXPENSE_DATA = ' + OUTPUT_JSON.read_text(encoding='utf-8') + '\n'
    OUTPUT_JS.write_text(js_payload, encoding='utf-8')
    DASHBOARD_JS.write_text(js_payload, encoding='utf-8')
    print(f'Обновлено expenses-data.js (записей: {len(combined)})')


if __name__ == '__main__':
    main()
