.PHONY = help run clean


FILES = input output


.DEFAULT_GOAL = help


help:
	@echo "---------------HELP-----------------"
	@echo "To run the project type make run"
	@echo "To delete .pyc files run make clean"
	@echo "------------------------------------"
	
run:
	${PYTHON} src/bot.py.py


clean:
	rm -r *.pyc
	

