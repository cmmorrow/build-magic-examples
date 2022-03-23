from pathlib import Path
import sys

from pyarrow import csv
import pyarrow.feather as feather


def load_file(filename: Path):
    table = csv.read_csv(str(filename), parse_options=csv.ParseOptions(delimiter=';'))
    feather_file = f'{filename.stem}.feather'
    feather.write_feather(table, f'{feather_file}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("CSV file path is required.")
        sys.exit(1)
    try:
        fn = Path(sys.argv[1]).resolve()
    except Exception:
        print(f"Cannot load file.")
        sys.exit(1)
    load_file(fn)
