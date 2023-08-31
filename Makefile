install:
	pip install -r requirements.txt

test:
	python -m unittest discover tests/

lint:
	pylint your_module/

format:
	black your_module/

.PHONY: install test lint format
