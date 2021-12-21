# django-delights makefile
.PHONY: requirements upgrade

PIP_COMPILE = pip-compile --rebuild --upgrade



requirements:
	pip install -r requirements/requirements.txt

upgrade:
	pip install -qr requirements/requirements.txt
	$(PIP_COMPILE) -o requirements/requirments.txt requirements/requirements.in

secret:
	python -c 'from django.core.management.utils import get_random_secret_key; \
            print("SECRET_KEY=" + get_random_secret_key())' > delights/.env
