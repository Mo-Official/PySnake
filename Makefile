
# SOURCE: https://medium.com/aigent/makefiles-for-python-and-beyond-5cf28349bf05
# define the name of the virtual environment directory
VENV := env

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

run: venv
	clear
	python3 Alchemist_Town.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

test:
	./$(VENV)/bin/python3 -m unittest tests/test*.py

req:
	./$(VENV)/bin/pip freeze > requirements.txt


.PHONY: all venv run clean test req