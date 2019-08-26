#!/usr/bin/env python3
"""Creates a PDF with images"""
import sys as system
import os as styresystem
åbn = open

HOVED = r"""
\documentclass[12pt,a4]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[danish]{babel}
\usepackage{graphicx}
%\usepackage{tgbonum}
\pagenumbering{gobble}
\usepackage{tikzpagenodes}
%\fontfamily{qcr}\selectfont
\usepackage{aurical}
\usepackage[T1]{fontenc}
\begin{document}
"""

FOD = r"""
\end{document}
"""

SKABELON = r"""
\begin{tikzpicture}[remember picture,overlay,shift={(current page.north east)}]
\centering
\node[anchor=north east,xshift=-0.15cm,yshift=0.5cm]{\includegraphics{ramme.png}};
\end{tikzpicture}
\begin{center}
\Fontauri
\end{center}
\begin{tikzpicture}[remember picture,overlay]
\node[anchor=north
east,xshift=13.9cm,yshift=2.2cm]{\includegraphics[width=\textwidth,trim={100pt 0
100pt 0},clip]{example-image-a}};
\end{tikzpicture}
\clearpage
"""

TEKST = HOVED
for FIL in system.stdin.read().split("\n")[:-1]:
    TEKST += SKABELON.replace("example-image-a", FIL)
TEKST += FOD

UD_FIL_BASE = "samlet"
with åbn(f"{UD_FIL_BASE}.tex", "w") as f:
    f.write(TEKST)

styresystem.system(f"latexrun {UD_FIL_BASE}.tex")
styresystem.system(f"rm {UD_FIL_BASE}.tex")
styresystem.system("rm -rf latex.out")
