"""Document index demo (text PDFs only, candidate values require review)."""
import argparse, csv, re
from pathlib import Path
from pypdf import PdfReader

MODEL_RE = re.compile(r"\b[A-Z]{1,5}[- ]?\d{2,6}[A-Z0-9-]*\b", re.I)

def models_from_text(text):
    return sorted({m.group(0).upper().replace(' ', '-') for m in MODEL_RE.finditer(text or '')})

def index(directory):
    result=[]
    for path in sorted(Path(directory).rglob('*.pdf')):
        try:
            reader=PdfReader(str(path))
            text='\n'.join(page.extract_text() or '' for page in reader.pages)
            for model in models_from_text(text):
                result.append({'model':model,'source':str(path)})
        except Exception as exc:
            print(f'Skipping {path.name}: {type(exc).__name__}: {exc}')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--directory',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    rows=index(a.directory);out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=['model','source']);w.writeheader();w.writerows(rows)
    print(f'Indexed {len(rows)} model/source pairs')
