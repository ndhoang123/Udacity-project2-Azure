install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py

setup:
	python3 -m venv ~/.udacity-devops

lint:
	pylint --disable=R,C hello.py

all: install lint test