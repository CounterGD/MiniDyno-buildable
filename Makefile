.PHONY: run docker build clean
run:
	python bot.py
docker:
	docker build -t minidyno:latest .
build: docker
clean:
	rm -rf __pycache__ *.pyc
