# Task Manager 
### A web application for managing tasks

[![Actions Status](https://github.com/Konst-Pav/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Konst-Pav/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/283a61003643f7eec2bf/maintainability)](https://codeclimate.com/github/Konst-Pav/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/283a61003643f7eec2bf/test_coverage)](https://codeclimate.com/github/Konst-Pav/python-project-52/test_coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)



The application was created using the Django framework. Allows you to create tasks, mark performers and the status of completion. To work, you need to register and log in.

### Installation:
The project uses <code>[Poetry](https://python-poetry.org/docs/)</code> to manage dependencies.
To set up a project, follow these steps:
1. Clone the repository 
   ```
   https://github.com/Konst-Pav/python-project-52
   ```
2. To set up an environment for a project, you need to define the environment variables in the .env file:
   ```
   SECRET_KEY=''
   DEBUG=False (either True for debugging mode)
   DATABASE_URL='' (the URL of the database)
   STATIC_URL='' (specify the path to the directory with static files)
   ROLLBAR_ACCESS_TOKEN='' (for the error tracking service https://docs.rollbar.com/docs/access-tokens)
   ```
3. In the project directory, run the following commands:
   ```
   poetry install
   make migrations
   make migrate
   ```
4. To run the tests and linter, use the following commands:
   ```
   make test
   make lint
   ```
5. To run the application locally, run the following command:
   ```
   make run_local_server
   ```

### Build With:
- Python
- Django
- Bootstrap 5
- PostgreSQL
- Poetry
- Gunicorn
- Rollbar
- Flake8
