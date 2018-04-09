.PHONY: clean, compile

compile: data.py
	python3 data.py

clean:
	rm -rf __pycache__
