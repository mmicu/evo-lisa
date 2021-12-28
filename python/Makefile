.DEFAULT_GOAL := test

.PHONY: linter
linter:
	flake8

.PHONY: type-checker
type-checker:
	mypy

.PHONY: sort-packages
sort-packages:
	isort .

.PHONY: test
test: linter type-checker
