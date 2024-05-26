main:
	latexmk -pvc main
.PHONY: main
plot:
	while :; do inotifywait -e modify,close_write,move $$(fd .py); make plot-build; done
.PHONY: plot
plot-latex:
	while :; do inotifywait -e modify,close_write,move $$(fd .py); make plot-build-latex; done
.PHONY: plot-latex
plot-build:
	python plot.py
.PHONY: plot-build
plot-build-latex:
	TEXINPUTS=$$(pwd): MATPLOTLIBRC=matplotlibrc.ondemand python plot.py
.PHONY: plot-build-latex
clean:
	latexmk -c
	rm -f *.log *.run.xml *.synctex *.toc
	rm -rf __pycache__
.PHONY: clean
ipython:
	ipython
.PHONY: ipython
ipython-latexplot:
	TEXINPUTS=$$(pwd): MATPLOTLIBRC=matplotlibrc.ondemand ipython
.PHONY: ipython-latexplot
