install:
	pip install --upgrade pip && pip install -r requirements/base.txt
install-dev:
	pip install --upgrade pip && pip install -r requirements/dev.txt
format:
	black core/*.py tests/*.py
lint:
	pylint --disable=R,C core/*.py tests/*.py
test:
	 python -m pytest -vv --cov=lib --cov=core tests/test_*.py
all: install format lint test
