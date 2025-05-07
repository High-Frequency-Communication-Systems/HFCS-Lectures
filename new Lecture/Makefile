%.pdf : %.md src/*.c
	gpp -T $< | pandoc -f markdown -t beamer --pdf-engine=lualatex -o $@ -H head.tex

%.tex : %.md
	gpp -T $< -o $*.tmp.md
	pandoc -f markdown $*.tmp.md -s -R -t beamer --pdf-engine=lualatex -o $@ -H head.tex

all: L1.pdf

tex: L1.tex

clean:
	rm L1.pdf
