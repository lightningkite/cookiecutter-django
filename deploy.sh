rm -rf project_name && \
	yes "" | cookiecutter . && \
	cd project_name && \
	# pip install -r requirements/production.txt && \
	python manage.py migrate && \
	gunicorn wsgi