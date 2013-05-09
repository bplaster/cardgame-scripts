#!/usr/bin/python

"""Produces TeX and PDF for a Char Card. Returns filename."""

import subprocess

LATEX_HEADER = """\\documentclass{article}
\\thispagestyle{empty}
\\usepackage[top=0.2in,bottom=0.2in,left=0.2in,right=0.2in,paperwidth=2.4in,paperheight=3.4in]{geometry}
\\usepackage[parfill]{parskip}
\\usepackage{wrapfig}
\\usepackage{graphicx}
\\usepackage{rotating}

\\begin{document}
	\\begin{sideways}
		\\begin{minipage}[2.4in]{3in}
			\\textbf{'State' Driver License}\\\\
"""

LATEX_IMAGE_HEADER = """	\\begin{wrapfigure}{l}{0.4\\linewidth}
		\\vspace{-0.25in}
		\\includegraphics[width=1.2in]{"""
		
LATEX_IMAGE_FOOTER = """}
		\\vspace{-0.35in}
	\\end{wrapfigure}
"""

LATEX_FOOTER = """
		\\end{minipage}
	\\end{sideways}
\\end{document}"""

def generate(card):
	# Generate output latex.
	qnty = int(card[0])
	name = str(card[1])
	titl = str(card[2])
	ador = str(card[3])
	soph = str(card[4])
	dext = str(card[5])
	spec = str(card[6])
	pkmy = str(card[7])
	#text = str(card[8])

	dir = './cards/'
	ext = '.tex'
	path = dir + name
	with open(path + ext, 'w') as out:
		out.write(LATEX_HEADER)
		out.write(LATEX_IMAGE_HEADER + dir + 'square.png' + LATEX_IMAGE_FOOTER)
		out.write('	FN: ' + titl + '\\\\\\\\[0.02in]\n')
		out.write('	Adorability: ' + ador + '\\\\\n')
		out.write('	Sophistication: ' + soph + '\\\\\n')
		out.write('	Dexterity: ' + dext + '\\\\\n')
		out.write('	Pocket Money: ' + pkmy + '\\\\\\\\[0.02in]\n')
		if (spec): out.write('	Special: ' + spec + '\\\\\n')
		#out.write('	Text: ' + text)
		out.write(LATEX_FOOTER)
	subprocess.call(['pdflatex','--output-directory=' + dir,path])
	return path, qnty