# Product Specification Indexer — Portfolio Demonstration

A **sanitized demonstration** of structured model extraction and search from documents. Inspired by my professional work processing 3,700+ product specification PDFs and assembling an index of approximately 240,000 models. **Not a copy of the production system.**

## Features
- Extracts selectable text from PDF files using `pypdf`
- Identifies candidate model numbers with a configurable pattern
- Normalizes and deduplicates candidate models
- Exports CSV with source-document provenance
- Optional simple CLI search over exported results

## Installation and use
```bash
python -m pip install -r requirements.txt
python src/index.py --directory sample_pdfs --output out/index.csv
python src/search.py --index out/index.csv --query AB-123
python -m unittest discover -s tests -v
```

Create your own nonconfidential test PDFs in `sample_pdfs/`. This demonstration handles text PDFs, **not OCR scans**, and extracted strings are *candidates* requiring review.

## Next steps
Coordinate-aware extraction; metadata validation; confidence scoring; OCR fallback; performance benchmarks.

## Security
No original employer PDFs, protected price lists, customer data or proprietary models are included.
