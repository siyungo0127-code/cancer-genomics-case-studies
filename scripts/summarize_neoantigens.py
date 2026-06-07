#!/usr/bin/env python3
"""Summarise an example tumour neoantigen CSV file.

This script intentionally stays lightweight: it summarises the included
example table but does not perform upstream neoantigen prediction.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


DEFAULT_INPUT = Path("data/example/StrongTumorNeoantigens_Stats.csv")
DEFAULT_OUTPUT = Path("results/neoantigen_summary.csv")

REQUIRED_COLUMNS = {
    "Tumour",
    "Gene_Symbol",
    "HLA_allele",
    "Mut_peptide",
    "Norm_MHCrank_EL",
    "Mut_MHCrank_EL",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a compact summary of the included neoantigen example CSV."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Input CSV path.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output CSV path.")
    return parser.parse_args()


def load_rows(input_path: Path) -> list[dict[str, str]]:
    with input_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED_COLUMNS.difference(reader.fieldnames or [])
        if missing:
            missing_text = ", ".join(sorted(missing))
            raise ValueError(f"Input CSV is missing required columns: {missing_text}")
        return list(reader)


def summarise(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    tumour_counts: Counter[str] = Counter()
    tumour_hlas: dict[str, set[str]] = defaultdict(set)
    tumour_genes: dict[str, set[str]] = defaultdict(set)
    tumour_best_rank: dict[str, float] = {}

    for row in rows:
        tumour = row["Tumour"]
        tumour_counts[tumour] += 1
        tumour_hlas[tumour].add(row["HLA_allele"])
        tumour_genes[tumour].add(row["Gene_Symbol"])

        mut_rank = float(row["Mut_MHCrank_EL"])
        if tumour not in tumour_best_rank or mut_rank < tumour_best_rank[tumour]:
            tumour_best_rank[tumour] = mut_rank

    summary_rows = []
    for tumour in sorted(tumour_counts):
        summary_rows.append(
            {
                "Tumour": tumour,
                "candidate_neoantigens": str(tumour_counts[tumour]),
                "unique_genes": str(len(tumour_genes[tumour])),
                "hla_alleles": ";".join(sorted(tumour_hlas[tumour])),
                "best_mut_mhcrank_el": f"{tumour_best_rank[tumour]:.4f}",
            }
        )

    return summary_rows


def write_summary(summary_rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "Tumour",
        "candidate_neoantigens",
        "unique_genes",
        "hla_alleles",
        "best_mut_mhcrank_el",
    ]
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary_rows)


def main() -> None:
    args = parse_args()
    rows = load_rows(args.input)
    summary_rows = summarise(rows)
    write_summary(summary_rows, args.output)
    print(f"Wrote {len(summary_rows)} tumour summaries to {args.output}")


if __name__ == "__main__":
    main()
