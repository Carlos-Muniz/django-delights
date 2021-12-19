# django-delights makefile

PIP_COMPILE = pip-compile --rebuild --upgrade

requirements:
	pip install -r requirements.txt

upgrade:
	pip install -qr requirements.txt
	$(PIP_COMPILE) -o requirements.txt requirements.in

secret:
	python -c 'from django.core.management.utils import get_random_secret_key; \
            print("SECRET_KEY=" + get_random_secret_key())' > delights/.env
