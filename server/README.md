# Server App

## Dependencies

* This project depends on python version `3.6.4`. It is recommended to install using `pyenv`. See step 2.

* Download and install [pyenv](https://github.com/pyenv/pyenv). Once installed ensure your `.bashprofile`
contains the following:
```
export PATH="/Users/username/.pyenv:$PATH"
eval "$(pyenv init -)"
```
`username` is the name on your system. Now cd into the server directory and change your `pyenv` version to `3.6.4`. To install this version run `pyenv install 3.6.4` and then run `pyenv local 3.6.4`.
* This application utilizes [poetry](https://github.com/sdispater/poetry). Please visit for installation instructions.
It is also recommended that `pyenv` is installed. It is recommended that you set your `.venv` to the project directory. You can
accomplish this by doing `poetry config settings.virtualenvs.in-project true`.

## Development

* Run `make install` to install all the dependencies.
* To setup sqlite databases run `make sql-migrate`. For verification your project is configured correctly run
`make test`. All tests should pass.
* To load sample data into the db run `make init-data`.
* To start server run `make start-server`.

## API Documentation
* While the server is running (see steps above), navigate to `http://127.0.0.1:8000/docs/` to see all endpoints. Or you
can navigate to the docs directory to see a pdf version.