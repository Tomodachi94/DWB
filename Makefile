.PHONY = help run clean


FILES = input output


.DEFAULT_GOAL = help


help:
	@echo "---------------HELP-----------------"
	@echo "To run the project type make run"
	@echo "To delete .pyc files run make clean"
  @echo "To initialize a working environment run make init"
	@echo "------------------------------------"
	
run:
	python src/bot.py


clean:
	rm -r *.pyc

init:
  cp assets/template/.env-template .env
  @echo "Please make sure to edit .env with your preferred settings."
	

