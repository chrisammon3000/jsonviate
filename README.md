# jsonviate
Map JSON records and define cross-references for Weaviate classes.

## Table of Contents

## Description

### Mapping Specification

### Cross-Reference Specification

## Installation

### Prerequisites
* Python 3.11
* Poetry

### Creating a Python Virtual Environment
When developing locally, first install the depndencies using Poetry.
```bash
poetry install
```
Then, activate a Python virtual environment to work within.
```bash
poetry shell
```

### Notebook Setup
To use the virtual environment inside Jupyter Notebook, first activate the virtual environment, then create a kernel for it.
```bash
# Install ipykernal and dot-env
pip install ipykernel python-dotenv

# Add the kernel
python3 -m ipykernel install --user --name=<environment name>

# Delete the kernel
jupyter kernelspec uninstall <environment name>
```

<!-- ### Environment Variables
Sensitive environment variables containing secrets like passwords and API keys must be exported to the environment first.

Create a `.env` file in the project root.
```bash
```

***Important:*** *Always use a `.env` file or AWS SSM Parameter Store or Secrets Manager for sensitive variables like credentials and API keys. Never hard-code them, including when developing. AWS will quarantine an account if any credentials get accidentally exposed and this will cause problems.*

***Make sure that `.env` is listed in `.gitignore`*** -->

## Testing
### Unit Tests
Create a Python virtual environment to manage test dependencies.

```bash
python3 -m venv .venv-test
source .venv-test/bin/activate
pip install -U pip
pip install -r requirements-tests.txt
```
Run tests with the following command.
```bash
coverage run -m pytest  
```

## Troubleshooting
* Check that the environment variables have been exported
* Check that the correct interpreter is being used for Python 3.11

## References & Links

## Authors
**Primary Contact:** Gregory Lindsey