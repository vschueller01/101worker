include ../Makefile.vars
output = ${ontoDir}

all:
	make run

run:
	cp disjointness.txt ${output}
	cp disjointness.rdf ${output}
	python pysesame.py
	mv subtyping_errors.json ${dumpsDir}
	cp -r tmpl ${output}/queries

# Remove local temporary files, if any
clean:
	@#no-op

# Remove files created by this module
reset:
	@#no-op
