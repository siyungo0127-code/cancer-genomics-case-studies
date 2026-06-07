# Cancer Genomics Case Studies

Portfolio repository for cancer genomics analysis case studies, with a focus on mutation interpretation, neoantigen prioritisation, tumour evolution concepts, technical reporting, and reproducible software habits. The repository currently includes a cancer genomics report artifact and a small example neoantigen summary table that can be inspected with a lightweight Python script.

## Why This Matters

Cancer genomics software helps researchers and clinicians interpret tumour sequencing data, identify candidate driver genes or mutations, prioritise variants for follow-up, and communicate results in a reproducible way. This repository is intended to show practical familiarity with cancer genomics workflows while being transparent about which artifacts are included and which upstream datasets are not redistributed.

## Skills Demonstrated

- Cancer genomics concepts: somatic variation, copy number alteration, tumour evolution, clonality, immune microenvironment analysis, and neoantigen prediction.
- Bioinformatics workflow awareness: separating raw data, scripts, results, reports, and documentation.
- Python software development: command-line script, standard-library CSV parsing, summary output, and basic validation.
- Reproducibility: explicit data limitations, example data location, and generated result files.
- Technical communication: recruiter-facing project summary and report-oriented documentation.
- GitHub collaboration readiness: clear repository structure, `.gitignore`, license, and run instructions.

## Repository Structure

```text
.
├── data/
│   ├── README.md
│   └── example/
│       └── StrongTumorNeoantigens_Stats.csv
├── docs/
│   └── project_summary.md
├── reports/
│   ├── Cancer_Genomics_CAM7032.pdf
│   └── README.md
├── results/
│   └── neoantigen_summary.csv
├── scripts/
│   └── summarize_neoantigens.py
├── .gitignore
├── LICENSE
└── README.md
```

## Case Studies And Included Artifacts

### Cancer Genomics Report

- Artifact: `reports/Cancer_Genomics_CAM7032.pdf`
- Scope: report-style cancer genomics case study work covering analysis themes such as copy number alteration, tumour evolution, immune microenvironment characterisation, neoantigen prediction, and tumour clonality.
- Reproducibility note: the PDF is included as a report artifact. The full upstream raw datasets and original analysis notebooks or pipeline outputs are not included in this repository.

### Neoantigen Summary Example

- Input: `data/example/StrongTumorNeoantigens_Stats.csv`
- Script: `scripts/summarize_neoantigens.py`
- Output: `results/neoantigen_summary.csv`
- Scope: small example summary of candidate strong tumour neoantigen records by tumour, HLA allele, and gene.
- Reproducibility note: this script summarises the included CSV only. It does not perform primary HLA typing, somatic variant calling, peptide generation, binding prediction, or clinical interpretation.

## How To Run

The included Python script uses only the Python standard library.

```bash
python3 scripts/summarize_neoantigens.py
```

By default, the script reads:

```text
data/example/StrongTumorNeoantigens_Stats.csv
```

and writes:

```text
results/neoantigen_summary.csv
```

You can also provide custom paths:

```bash
python3 scripts/summarize_neoantigens.py \
  --input data/example/StrongTumorNeoantigens_Stats.csv \
  --output results/neoantigen_summary.csv
```

## Limitations And Reproducibility Notes

- Raw clinical, sequencing, and controlled-access genomic datasets are not included.
- Large intermediate files such as FASTQ, BAM, CRAM, VCF, MAF, count matrices, and model outputs are intentionally excluded.
- The repository should not be described as a complete end-to-end production NGS pipeline.
- The included script provides a reproducible summary of the example CSV; it does not reproduce upstream neoantigen prediction.
- Reported biological interpretations should be treated as case-study outputs, not clinical recommendations.

## Relevance To Cancer Genomics Software Development

This repository demonstrates the kind of organisation expected in collaborative bioinformatics software work: clear inputs and outputs, lightweight automation, documentation for non-specialists, separation of reports from data, and transparent limitations. These habits are directly relevant to cancer patient mutation analysis, driver mutation interpretation workflows, pipeline development, and reproducible technical reporting.

## Recruiter Summary

This project presents cancer genomics case studies in a clean GitHub structure, with transparent documentation, a small reproducible Python example, and a technical report artifact. It is most relevant to roles involving bioinformatics software development, cancer mutation analysis, NGS workflow support, reproducibility, and scientific communication.
