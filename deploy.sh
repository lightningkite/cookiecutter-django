rm -rf project_name && \
	yes "" | cookiecutter . && \
	cd project_name && \
	python manage.py migrate && \
	gunicorn config/wsgi.py