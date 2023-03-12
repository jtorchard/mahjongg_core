install:
	pip install --upgrade pip && pip install -r requirements/base.txt
install-dev:
	pip install --upgrade pip && pip install -r requirements/dev.txt
format:
	black *.py
lint:
	pylint --disable=R,C *.py
test:
	 python -m pytest -vv --cov=lib --cov=core tests/test_*.py
all: install format lint tests
