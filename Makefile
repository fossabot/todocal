.PHONY: clean, compile

compile: data.py time.py handler.py
	python3 data.py
	python3 time.py
	python3 handler.py

clean:
	rm -rf __pycache__
