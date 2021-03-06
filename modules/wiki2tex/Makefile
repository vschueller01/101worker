include ../Makefile.vars

run:
	make up
	make content
	make dump
	make publish	
all:
	make up
	make local

local:
	make clean
	make content-only
	make onto-only
	make matrix-only
	make dump-only
up:
	git pull
	cd ../../libraries; git pull

content:
	make up
	make content-only

content-only:
	mkdir -p tex/content/latex
	php texgenerator.php --mode=content
	cd tex/content/latex; make

onto:
	make up
	mkdir -p tex/ontology/data/classification/
	make onto-only

onto-only:
	mkdir -p tex/ontology/latex
	php texgenerator.php --mode=ontology
	cd tex/ontology/latex; make

matrix:
	make up
	make matrix-only

matrix-only:
	php texgenerator.php --mode=matrixif --output=matrixif
	php texgenerator.php --mode=matrixis --output=matrixis
	php texgenerator.php --mode=matrixts --output=matrixts
	make matrix-pppj
	cd tex/matrix/latex; make

matrix-pppj:
	php texgenerator.php --mode=matrixif --ilist=../lists/pppjImpls.lst --output=pppjif
	php texgenerator.php --mode=matrixts --tlist=../lists/pppjTechs.lst --output=pppjts

dump:
	make up
	make dump-only

dump-only:
	mkdir -p tex/dump/latex
	mkdir -p tex/dump/data	
	php texgenerator.php --mode=dump
	cd tex/dump/latex; make

publish:
	tar -cvvf tex.tar tex
	rm -r ${webdir}/texgen
	mkdir -p ${webdir}/texgen
	#cp -r -f tex ${webdir}/texgen
	cp tex.tar ${webdir}/texgen
	
clean:
	rm -f tex/files/*.ext
	cd tex/content/latex; make clean
	cd tex/content/data; make clean
	cd tex/dump/latex; make clean
	cd tex/dump/data; make clean
	rm tex.tar
