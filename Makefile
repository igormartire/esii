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
