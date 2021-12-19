# django-delights makefile

PIP_COMPILE = pip-compile --rebuild --upgrade

requirements:
	pip install -r requirements.txt

upgrade:
	pip install -qr requirements.txt
	$(PIP_COMPILE) -o requirements.txt requirements.in


