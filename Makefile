.PHONY: clean, compile, manual

compile: tc_data.py tc_time.py tc_handler.py tc_print.py tc_display.py tc_meta.py
	python3 tc_data.py
	python3 tc_time.py
	python3 tc_handler.py
	python3 tc_print.py
	python3 tc_display.py
	python3 tc_meta.py
	make clean

clean:
	rm -rf __pycache__

manual:
	python3
	make clean
