install:
	@poetry install

build:
	@poetry build

test:
	@poetry run python manage.py test

wheel:
	@poerty build -v

sql-migrate:
	@poetry run python manage.py makemigrations
	@poetry run python manage.py migrate

start-server:
	@poetry run python manage.py runserver
