"""Load the Data in Brief repository tables and run basic integrity checks."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

def rows(relpath):
    with open(ROOT / relpath, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

matrix = rows('data/design/full_factorial_design_48.csv')
assert len(matrix) == 48, f"Expected 48 factorial combinations, got {len(matrix)}"
assert sum(int(r['planned_request_count']) for r in matrix) == 15552

means = rows('data/processed/backend_mode_cell_means.csv')
assert len(means) == 12, f"Expected 12 backend x mode cells, got {len(means)}"

failures = rows('data/processed/failure_taxonomy_overall.csv')
assert sum(int(r['count']) for r in failures) == 15552

print('Integrity checks passed: 48 combinations, 15,552 planned requests, 12 backend-mode cells, and failure counts sum to total request count.')
