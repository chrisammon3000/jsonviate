# include .env

.PHONY: install
install: ## Install the poetry environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install	
	@poetry run pre-commit install
	@poetry run pre-commit autoupdate
	@poetry shell

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry lock --check
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
# @echo "🚀 Static type checking: Running mypy"
# @poetry run mypy

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest -v --cov --cov-config=pyproject.toml

.PHONY: build
build: clean-build ## Build wheel file using poetry
	@echo "🚀 Creating wheel file"
	@poetry build	

.PHONY: clean-build
clean-build: ## clean build artifacts
	@rm -rf dist

publish:
	$(MAKE) publish.codeartifact

.PHONY: publish.pypi
publish.pypi: ## publish a release to pypi.
	@echo "🚀 Publishing: Dry run."
	@poetry config pypi-token.pypi $(PYPI_TOKEN)
	@poetry publish --dry-run
	@echo "🚀 Publishing."
	@poetry publish

.PHONY: publish.codeartifact
publish.codeartifact: ## publish a release to AWS CodeArtifact.
	@echo "🚀 Publishing: Dry run."
	@poetry publish --dry-run
	@echo "🚀 Publishing."
	@poetry publish --repository "${REPOSITORY}"

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help