start:
	python ./src/main.py

test:
	cd src && python -m pytest ../tests && cd ..

lint:
	black src