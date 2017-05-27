run:
	python -m chess

pep:
	pep8 chess/ tests/

test:
	python -m pytest tests/

clean:
	find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf