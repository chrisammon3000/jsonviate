# Makefile for formatting and linting a Python package using poetry

# Path to the package
PACKAGE_PATH = .

# This is the default target
all:
	@echo "Please specify a target"

# Target for formatting the package with black
format:
	poetry run black $(PACKAGE_PATH)

# Target for linting the package with flake8
lint:
	poetry run flake8 $(PACKAGE_PATH)
	

# Define a target to run the tests
test:
	@poetry run coverage run --source=src -m pytest -v tests && coverage report -m
