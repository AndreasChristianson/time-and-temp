.PHONY: run clean pull

run:
	python3 src/time-and-temp.py

pull:
	git pull 

setup: requirements.txt
	pip3 install -r requirements.txt

clean:
	rm -rf __pycache__