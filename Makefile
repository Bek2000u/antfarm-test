install:
	pip install -r requirements.txt

test:
	pytest

run:
	uvicorn main:app --reload
