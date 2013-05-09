#!/usr/bin/python

"""Produces TeX and PDF for a Play Card. Returns filename."""

import subprocess

LATEX_HEADER = """\\documentclass{article}
\\thispagestyle{empty}
\\usepackage[top=0.25in,bottom=0.25in,left=0.2in,right=0.2in,paperwidth=2.4in,paperheight=3.4in]{geometry}
\\usepackage[parfill]{parskip}
\\usepackage{wrapfig}
\\usepackage{graphicx}

\\begin{document}
"""

LATEX_IMAGE_HEADER = """	\\begin{wrapfigure}{r}{0.6\\linewidth}
		\\vspace{-0.7in}
		\\includegraphics[width=1.3in]{"""
		
LATEX_IMAGE_FOOTER = """}
		\\vspace{-1in}
	\\end{wrapfigure} \\\\[0.75in]
"""

LATEX_FOOTER = """
\\end{document}"""

def generate(card):
	# Generate output latex.
	qnty = int(card[0])
	name = str(card[1])
	titl = str(card[2])
	type = str(card[3])
	styp = str(card[4])
	efct = str(card[5])
	ador = str(card[6])
	soph = str(card[7])
	dext = str(card[8])
	cost = str(card[9])
	#text = str(card[10])

	dir = './cards/'
	ext = '.tex'
	path = dir + name
	with open(path + ext, 'w') as out:
		out.write(LATEX_HEADER)
		out.write('	\\textbf{' + titl + '}\\\\\n')
		out.write('	' + type + '\\\\\n')
		out.write('	' + styp + '\\\\\n')
		out.write('	Cost: ' + cost + '\\\\\n')
		out.write(LATEX_IMAGE_HEADER + dir + 'square.png' + LATEX_IMAGE_FOOTER)
		if (ador): out.write('	Adorability: ' + ador + '\\\\\n')
		if (soph): out.write('	Sophistication: ' + soph + '\\\\\n')
		if (dext): out.write('	Dexterity: ' + dext + '\\\\\n')
		if (efct): out.write('	Effect: ' + efct + '\\\\\n')
		#out.write('	\\vfill \n' + '	Text: ' + text)
		out.write(LATEX_FOOTER)
	subprocess.call(['pdflatex','--output-directory=' + dir,path])
	return path, qnty