.PHONY: run clean pull

run: venv/bin/activate
	python3 src/update_eink.py

dev:
	python3 src/display_image.py

pull:
	git pull 

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf venv