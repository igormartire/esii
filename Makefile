run:
	python -m chess

pep:
	pep8 chess/ tests/

autopep:
	make pep | grep -o '^.*py' | xargs autopep8 --in-place

test:
	python -m pytest tests/

clean:
	find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf

.PHONY: unbuild
unbuild:
	rm -rf build
	rm -rf dist

.PHONY: build
build:
	rm -rf build
	rm -rf dist
	python setup.py py2app
