install:
	pip install --upgrade pip && pip install -r requirements/base.txt
install-dev:
	pip install --upgrade pip && pip install -r requirements/dev.txt
format:
	ruff format
lint:
	ruff check -v
test:
	 python -m pytest -vv --cov=src --cov=tests tests/test_*.py
all: install format lint test
