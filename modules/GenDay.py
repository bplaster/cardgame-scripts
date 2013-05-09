#!/usr/bin/python

"""Produces TeX and PDF for a Day Card. Returns filename and count."""

import subprocess

LATEX_HEADER = """\\documentclass{article}
\\thispagestyle{empty}
\\usepackage[top=0.25in,bottom=0.25in,left=0.2in,right=0.2in,paperwidth=2.4in,paperheight=3.4in]{geometry}
\\usepackage[parfill]{parskip}
\\usepackage{graphicx}

\\begin{document}
	\\centering
"""

LATEX_IMAGE_HEADER = """		\\includegraphics[width=2in,height=1.2in]{"""
		
LATEX_IMAGE_FOOTER = """}\\\\[0.05in]
"""

LATEX_FOOTER = """
\\end{document}"""

def generate(card):
	# Generate output latex.
	qnty = int(card[0])
	name = str(card[1])
	titl = str(card[2])
	bank = str(card[3])
	lawm = str(card[4])
	beg = str(card[5])
	borr = str(card[6])
	stea = str(card[7])
	spec = str(card[8])
	#text = str(card[9])
	
	dir = './cards/'
	ext = '.tex'
	path = dir + name
	with open(path + ext, 'w') as out:
		out.write(LATEX_HEADER)
		out.write('	\\textbf{' + titl + '}\\\\\n')
		out.write(LATEX_IMAGE_HEADER + dir + 'square.png' + LATEX_IMAGE_FOOTER)
		out.write('	Bankers: ' + bank + '\\\\\n')
		out.write('	Lawmen: ' + lawm + '\\\\\n')
		out.write('	Beg: ' + beg + '\\\\\n')
		out.write('	Borrow: ' + borr + '\\\\\n')
		out.write('	Steal: ' + stea + '\\\\[0.05in]\n')
		out.write('	\\raggedright \n')
		if (spec): out.write('	Special: ' + spec + '\\\\\n')
		#out.write('	\\vfill \n' + '	Text: ' + text)
		out.write(LATEX_FOOTER)
	subprocess.call(['pdflatex','--output-directory=' + dir,path])
	return path, qnty