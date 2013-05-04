#!/usr/bin/python

"""Produces Master LaTeX document for all generated cards.

Arguments:
<play> - csv file of cards of type Play
<day> - csv file of cards of type Day
<char> - csv file of cards of type Character
<out> - optional output tex file name

example: python GenerateMaster.py -play PlayCards.csv 
"""

import argparse
import csv
import subprocess
from modules import GenPlay as gp
from modules import GenDay as gd
from modules import GenChar as gc


LATEX_HEADER = """\\documentclass{article}
\\usepackage[landscape, top=0.5in, bottom=0.5in, left=0.5in, right=0.5in]{geometry}
\\usepackage[parfill]{parskip}
\\usepackage{graphicx}

\\begin{document}"""

LATEX_CARD_HEADER = """
	\\begin{minipage}{0.25\\textwidth}
		\\frame{\\includegraphics{"""
  
LATEX_CARD_FOOTER = """}}
	\\end{minipage}"""

LATEX_FOOTER = """
\\end{document}"""

# Function that adds cards from file to list
def genCards(arg,module,list):
	if arg is not None:
		with open(arg, 'rU') as f:
			reader = csv.reader(f)
			next(reader, None) # skip the header
			for line in reader:
				cardname, count = module.generate(line) # generate specific card pdf/tex
				list.extend([cardname for _ in xrange(count)])
	return list

# Main function
def main():
  	parser = argparse.ArgumentParser()
	parser.add_argument('-play', metavar='CSV_FILE', type=str,
						help='csv file with card type: Play')
	parser.add_argument('-day', metavar='CSV_FILE', type=str,
						help='csv file with card type: Day')
	parser.add_argument('-char', metavar='CSV_FILE', type=str,
						help='csv file with card type: Character')
	parser.add_argument('-out', metavar='OUT_FILE', type=str, default='out.tex',
						nargs='?', help='optional output filename, defaults to out.tex')
	args = parser.parse_args()

	# Generate list of card minipages.
	cards = []
	cards = genCards(args.play,gp,cards) # Generate Play Cards
	cards = genCards(args.day,gd,cards)	# Generate Day Cards
	cards = genCards(args.char,gc,cards) # Generate Character Cards
				
	# Generate output latex.
	with open(args.out, 'w') as out:
		out.write(LATEX_HEADER)
		for index, card in enumerate(cards):
			out.write(LATEX_CARD_HEADER)
			out.write(card)
			out.write(LATEX_CARD_FOOTER)
			if (index + 1) % 4 == 0:
				out.write(' \\\[0.15in]')
		out.write(LATEX_FOOTER)
		
	# Generate output pdf
	subprocess.call(['pdflatex',args.out])


if __name__ == '__main__':
  main()
