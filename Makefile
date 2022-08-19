mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))

.PHONY: plots
plots:
	python3 src/easing_functions/plot_easing_funcs.py src/easing_functions/schedules.json

.PHONY: install-plots
install-plots:
	pip3 install -r src/easing_functions/requirements.txt