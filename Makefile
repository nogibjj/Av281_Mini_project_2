install:
	pip install -r requirements.txt

test:
	python -m pytest

lint:
	pylint 

format:
	black 

.PHONY: install test lint format
