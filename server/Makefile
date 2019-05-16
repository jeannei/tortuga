build:
	@poetry build

install:
	@poetry install

init-data:
	@poetry run python manage.py load

make-app:
	@cd tortuga/apps && poetry run django-admin startapp $(NAME)

sql-migrate:
	@poetry run python manage.py makemigrations && poetry run python manage.py migrate

start-server:
	@poetry run python manage.py runserver

test:
	@poetry run python manage.py test

wheel:
	@poetry build -v

