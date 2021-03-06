# django-delights makefile
.PHONY: requirements upgrade all migrate runserver clean shell

PIP_COMPILE = pip-compile --rebuild --upgrade

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

requirements: ## install development environment requirements
	pip install -r requirements/requirements.txt

upgrade: ## update the requirements/*.txt files with the latest packages satisfying requirements/*.in
	pip install -qr requirements/requirements.txt
	$(PIP_COMPILE) -o requirements/requirements.txt requirements/requirements.in

secret: ## create the random secret key necessary to run the server
	python -c 'from django.core.management.utils import get_random_secret_key; \
            print("SECRET_KEY=" + get_random_secret_key())' > delights/.env

migrate: ## makes migrations and migrates via django manage.py
	python delights/manage.py makemigrations
	python delights/manage.py migrate

runserver: ## runs the server via django manage.py
	python delights/manage.py runserver

clean: ## removes all created files for a blank slate
	rm -f delights/.env
	rm -f delights/*db.sqlite3
	rm -rf delights/*/__pycache__
	rm -rf delights/Inventory/migrations/0*
	rm -rf delights/Inventory/migrations/__pycache__

shell: ## creates a shell via django manage.py
	python delights/manage.py shell

import-demo: ## imports demo data via django manage.py
	python delights/manage.py loaddata demo.json

demo: clean requirements secret migrate import-demo runserver ## runs demo
