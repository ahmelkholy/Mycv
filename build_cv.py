"""Build the CV PDF and plain-text copy from the editable Markdown source.

Requires Python 3 and XeLaTeX (TeX Live). Run: python3 build_cv.py
Only the Markdown subset used by this CV is supported.
"""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent

def escape(value):
    mapping = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    return ''.join(mapping.get(c, c) for c in value)

def inline(value):
    pattern = r'(\[[^\]]+\]\([^)]+\)|\*\*[^*]+\*\*|\*[^*]+\*)'
    parts = re.split(pattern, value)
    out = []
    for part in parts:
        match = re.fullmatch(r'\[([^\]]+)\]\(([^)]+)\)', part)
        if match:
            label, url = match.groups()
            out.append(r'\href{' + escape(url) + '}{' + escape(label) + '}')
        elif part.startswith('**') and part.endswith('**'):
            out.append(r'\textbf{' + escape(part[2:-2]) + '}')
        elif part.startswith('*') and part.endswith('*'):
            out.append(r'\textit{' + escape(part[1:-1]) + '}')
        else:
            out.append(escape(part))
    return ''.join(out)

PREAMBLE = r'''\documentclass[10pt,a4paper]{article}
\usepackage[margin=16mm,top=14mm,bottom=16mm]{geometry}
\usepackage{fontspec}
\setmainfont{Arial}
\usepackage{xcolor,enumitem,titlesec,fancyhdr}
\usepackage[unicode,colorlinks=true,urlcolor=accent]{hyperref}
\definecolor{accent}{HTML}{24536E}
\hypersetup{pdftitle={Ahmed M. Elkholy - Curriculum Vitae},pdfauthor={Ahmed M. Elkholy}}
\titleformat{\section}{\large\bfseries\color{accent}}{}{0pt}{}[\titlerule]
\titlespacing*{\section}{0pt}{8pt}{4pt}
\setlist[itemize]{leftmargin=13pt,itemsep=1pt,topsep=2pt,parsep=0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}
\setlength{\headheight}{13pt}
\pagestyle{fancy}\fancyhf{}
\fancyfoot[L]{\footnotesize Ahmed M. Elkholy}
\fancyfoot[R]{\footnotesize \thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0.2pt}
\emergencystretch=3em
\begin{document}
\raggedright
'''

def main():
    source = (ROOT / 'CV_Ahmed_M_Elkholy.md').read_text()
    output = [PREAMBLE]
    in_list = False
    for line in source.splitlines():
        if not line.startswith('- ') and in_list:
            output.append(r'\end{itemize}')
            in_list = False
        if line == '<!-- pagebreak -->':
            output.append(r'\newpage')
        elif line.startswith('# '):
            output.append(r'{\LARGE\bfseries\color{accent} ' + inline(line[2:]) + r'}\par')
        elif line.startswith('## '):
            output.append(r'\section*{' + inline(line[3:]) + '}')
        elif line.startswith('- '):
            if not in_list:
                output.append(r'\begin{itemize}')
                in_list = True
            output.append(r'\item ' + inline(line[2:]))
        elif line.strip():
            output.append(inline(line) + r'\par')
    if in_list:
        output.append(r'\end{itemize}')
    output.append(r'\end{document}')
    (ROOT / 'Ahmed_M_Elkholy-cv.tex').write_text('\n'.join(output) + '\n')
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', source)
    text = text.replace('<!-- pagebreak -->', '').replace('*', '')
    (ROOT / 'CV_Ahmed_M_Elkholy.txt').write_text(text)
    for _ in range(2):
        subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', 'Ahmed_M_Elkholy-cv.tex'], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
    print('Built Ahmed_M_Elkholy-cv.pdf, .tex, and CV_Ahmed_M_Elkholy.txt')

if __name__ == '__main__':
    main()
