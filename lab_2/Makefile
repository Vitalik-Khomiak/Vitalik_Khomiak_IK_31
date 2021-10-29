.DEFAULT_GOAL := all

all: install test run deploy

install:
  @echo "Welcome to quick configuration"
	@echo "-----------A---r---t---L---A---B-----------"
	@echo "Installing pipenv and dependencies."
	@echo "-----------A---r---t---L---A---B-----------"
	sudo pip install pipenv
	sudo pipenv --python 3.8
	sudo pipenv install requests
	sudo pipenv install ntplib
	sudo pipenv install pytest

test:
	@echo "-----------A---r---t---L---A---B-----------"
	@echo "Start tests."
	@echo "-----------A---r---t---L---A---B-----------"
	sudo pipenv run pytest tests/tests.py > results.txt

run:
	@echo "-----------A---r---t---L---A---B-----------"
	@echo "Running Python app."
	@echo "-----------A---r---t---L---A---B-----------"
	sudo pipenv run python app.py >> results.txt

deploy:
	@echo "-----------A---r---t---L---A---B-----------"
	@echo "Adding and Committing results.txt to git."
	@echo "-----------A---r---t---L---A---B-----------"
	git add results.txt
	git commit -m "Automatic commit by MakeFile"
	git push
