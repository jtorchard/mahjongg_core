install:
	pip install --upgrade pip && pip install -r requirements/base.txt
install-dev:
	pip install --upgrade pip && pip install -r requirements/dev.txt
format:
	black core/*.py tests/*.py
lint:
	ruff check -v
test:
	 python -m pytest -vv --cov=lib --cov=core tests/test_*.py
all: install format lint test
