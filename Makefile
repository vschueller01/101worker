# Main target; run all modules

run:
	@echo Performing all modules.
	@make prepare -s
	@cd modules; make run -s
	@python tools/mailer.py


# Test target; run a few modules without logging

test:
	make testOkNoOp.run
	make testOkWrite.run
	make testOkReadWrite.run

# Run a specific module in sandbox mode

%.run: modules/%/Makefile
	cd modules/$*; make

# Reconfiguration for a module lists

%.reconfigure: configs/%.config
	@cd configs; \
	rm -f current.config; \
	cp $*.config current.config; \
	chmod ugo-w current.config

# Comprehensive clean target

clean:
	@make prepare -s
	@cd modules; make clean -s

# Internal target: prepare a run or even a clean

prepare:
	@git pull -q # upgrade before every run
	@make configs/current.config -s
	@make ../101logs -s
	@make ../101temps -s
	@make ../101results -s
	@rm -f ../101logs/runner.log

# Target for git-related convenience

push:
	git commit -a
	git push

# Internal target: use production configuration by default.

configs/current.config: configs/production.config
	make production.reconfigure -s

# Internal target: make sure 101logs directory exists.

../101logs:
	@mkdir ../101logs

# Internal target: make sure 101temps directory exists.

../101temps:
	@mkdir ../101temps

# Internal target: make sure 101results directory exists.

../101results:
	@mkdir ../101results
