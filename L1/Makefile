DOC  := lecture1.tex

all: src doc

figs:
	@$(MAKE) -C $@

doc: $(DOC:.tex=.pdf)

%.pdf: %.tex
	xelatex --shell-escape --synctex=1 $<
	@egrep -q $(RERUNBIB) $*.log && bibtex $* && xelatex --shell-escape --synctex=1 $<; true
	@egrep -q $(RERUN) $*.log && xelatex --shell-escape --synctex=1 $<; true
	@egrep -q $(RERUN) $*.log && xelatex --shell-escape --synctex=1 $<; true

latexmk:
	-latexmk -pvc -pdf $(DOC)

purge:
	-rm -f *.{aux,dvi,log,bbl,blg,brf,fls,toc,thm,out,fdb_latexmk}

clean: purge
	$(MAKE) -C figs $@
	-rm -f $(DOC:.tex=.pdf)

.PHONY: all figs purge clean
