# Cancer Genomics Case Studies

## Overview

This repository presents a collection of cancer genomics analyses performed using real-world genomic datasets.

The project covers several major areas of modern cancer bioinformatics:

* Copy Number Alteration (CNA) analysis
* Tumour evolution inference
* Neoantigen prediction
* Immune cell deconvolution
* Pathway enrichment analysis
* Tumour clonality reconstruction

The analyses demonstrate computational approaches widely used in cancer genomics research and precision oncology.

---

## Project 1 — Single-Cell Copy Number Evolution Analysis

### Objective

Investigate genomic instability in high-grade serous ovarian cancer (HGSOC) using single-cell whole-genome sequencing.

### Tools

* AneuFinder
* MEDICC2
* R
* Single-cell DNA sequencing

### Key Findings

* Copy number alterations were unevenly distributed across chromosomes.
* Most alterations were sub-chromosomal rather than whole-chromosome events.
* Snu119 clones showed longer evolutionary branch lengths than Kuramochi clones, suggesting higher genomic instability.

---

## Project 2 — Tumour Microenvironment Characterisation

### Objective

Estimate immune and stromal cell populations from bulk RNA-seq data.

### Methods

* xCell
* MCPcounter
* Decosus

### Key Findings

* Tumour samples showed stronger immune-related signatures.
* Increased T-cell and cytotoxic lymphocyte infiltration was observed in tumour tissues.
* Consensus deconvolution produced robust clustering patterns.

---

## Project 3 — Neoantigen Prediction

### Objective

Identify tumour-specific neoantigens for immunotherapy applications.

### Tools

* MuPeXi
* HLA-A02:01
* HLA-A24:02

### Key Findings

* Hundreds of tumour neoantigens were identified.
* Strong neoantigens varied substantially across patients.
* No shared neoantigens were detected between tumours, supporting personalised immunotherapy strategies.

---

## Project 4 — Tumour Clonality and Evolution

### Objective

Infer tumour evolutionary structure using variant allele frequencies.

### Tools

* mClust
* Gaussian Mixture Modelling

### Key Findings

* Multiple tumour subclones were identified.
* Distinct clonal populations exhibited different cancer cell fractions.
* Metastatic lymph node samples displayed evidence of divergent evolution.

---

## Skills Demonstrated

### Bioinformatics

* Cancer genomics
* Somatic mutation analysis
* Neoantigen prediction
* Tumour evolution
* Copy number analysis
* RNA-seq interpretation

### Programming

* R
* Data visualisation
* Statistical analysis

### Research

* Scientific interpretation
* Genomic data analysis
* Precision oncology concepts
