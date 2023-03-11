install:
	pip install --upgrade pip && pip install -r requirements/base.txt
install-dev:
	pip install --upgrade pip && pip install -r requirements/dev.txt
format:
	black *.py
lint:
	pylint --disable=R,C *.py
test:
	 pytest -vv --cov=lib --cov=main tests/test_*.py
all: install format lint test
