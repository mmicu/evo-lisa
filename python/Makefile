.PHONY: linter
linter:
	flake8

.PHONY: profiler
profiler:
	python3 -m cProfile -s time -m evo_lisa \
		../assets/input_images/Mona-Lisa.bmp _Mona-profiler.png -n 5000 \
		&> _profiler-output.txt

.PHONY: type-checker
type-checker:
	mypy

.PHONY: test
test: linter type-checker
