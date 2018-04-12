.PHONY: clean, compile, manual

compile: tc_data.py tc_time.py tc_handler.py
	python3 tc_data.py
	python3 tc_time.py
	python3 tc_handler.py

clean:
	rm -rf __pycache__

manual:
	python3
