.PHONY: all clean cover doc test deploy

help:
	@echo "Available commands:"
	@echo "  clean				remove temp files and static generated docs"
	@echo "  cover				generate test coverage"
	@echo "  doc				generate doc"
	@echo "  test				run all tests"
	@echo "  deploy				package and deploy code to PyPI"

install: clean
	pip install -e .[dev]

clean:
	find ./ -type f -name '*.pyc' -exec rm -f {} \;
	rm -rf cover .coverage
	rm -rf docs/build dist eggs

cover:
	ENV=test nosetests -s -v --with-coverage --cover-html --cover-html-dir ./coverage

test:
	ENV=test nosetests -s --nologcapture

all: clean

doc: clean
	sphinx-build -b html doc/source doc/build/html
	@echo
	livereload -b doc/build/html -p 3001

deploy:
	python setup.py sdist bdist_wininst upload
