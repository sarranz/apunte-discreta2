.PHONY:
	clean

abstract:
	[ -d latex ] || mkdir latex
	pdflatex -output-directory latex main.tex

clean:
	rm -rvf latex main.pdf
