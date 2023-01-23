main:
	latexmk -pvc main
.PHONY: main
plot:
	while :; do inotifywait -e modify,close_write,move $$(fd .py); make plot-build; done
.PHONY: plot
plot-build:
	TEXINPUTS=$$(pwd): MATPLOTLIBRC=matplotlibrc python plot.py
.PHONY: plot-build
clean:
	latexmk -c
	rm -f *.log *.run.xml *.synctex *.toc
	rm -rf __pycache__
.PHONY: clean
ipython:
	TEXINPUTS=$$(pwd): MATPLOTLIBRC=matplotlibrc ipython
.PHONY: ipython
