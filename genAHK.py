from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG_DIR = ROOT / "config"
NUM_CSV = CONFIG_DIR / "num.csv"
NUM_SYMBOL_CSV = CONFIG_DIR / "num_symbol.csv"
OUTPUT_FILE = ROOT / "include.ahk"


def read_two_column_csv(path: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            if len(row) < 2:
                raise ValueError(f"CSV format error in {path}: {row}")
            left = row[0].strip()
            right = row[1].strip()
            if left and right:
                rows.append((left, right))
    return rows


def generate_include_ahk(modifier: str = "vk1C") -> None:
    num = read_two_column_csv(NUM_CSV)
    num_symbol = read_two_column_csv(NUM_SYMBOL_CSV)

    lines: list[str] = []

    for c in range(len(num)):
        lines.append(
            f'{modifier} & {num[c][0]}:: Send("{{Blind}}{{NumPad{num[c][1]}}}")\n'
        )

    for c in range(len(num_symbol)):
        lines.append(
            f'{modifier} & {num_symbol[c][0]}:: Send("{{U+{num_symbol[c][1]}}}")\n'
        )

    OUTPUT_FILE.write_text("".join(lines), encoding="utf-8")


if __name__ == "__main__":
    generate_include_ahk()
