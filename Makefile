.PHONY: clean, compile, manual

compile: tc_data.py tc_time.py tc_handler.py tc_print.py tc_display.py tc_meta.py
	@echo 'compile with python 3'
	@python3 tc_data.py
	@python3 tc_time.py
	@python3 tc_handler.py
	@python3 tc_print.py
	@python3 tc_display.py
	@python3 tc_meta.py
	@echo 'compile with python 2'
	@python  tc_data.py
	@python  tc_time.py
	@python  tc_handler.py
	@python  tc_print.py
	@python  tc_display.py
	@python  tc_meta.py
	make clean

clean:
	rm -rf __pycache__
	rm -rf *.pyc

manual:
	python3
	make clean
