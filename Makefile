.PHONY: clean, compile, manual, display

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
	rm -rf *test*

manual:
	python3
	make clean

display: tc_display.py
	@touch test_display.py
	@echo '# This file is auto-generated by Makefile.' >> test_display.py
	@echo 'from tc_display import *' >> test_display.py
	@echo 'calendar = make_display()' >> test_display.py
	@echo 'for s in calendar:' >> test_display.py
	@echo '    print (s)' >> test_display.py
	@echo 'display with python 3'
	@python3 test_display.py
	@echo 'display with python 2'
	@python  test_display.py
	@rm -rf test_display.py
	make clean
