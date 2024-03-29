# Task Manager 
### A web application for managing tasks. <code>[Try it now](http://62.113.97.17/)</code>

[![Actions Status](https://github.com/Konst-Pav/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Konst-Pav/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/283a61003643f7eec2bf/maintainability)](https://codeclimate.com/github/Konst-Pav/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/283a61003643f7eec2bf/test_coverage)](https://codeclimate.com/github/Konst-Pav/python-project-52/test_coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)



The application was created using the Django framework. Allows you to create tasks, mark performers and the status of completion. To work, you need to register and log in.

### Installation:
Для управления зависимостями в проекте используется <code>[Poetry](https://python-poetry.org/docs/)</code>.
Чтобы настроить проект, выполните следующие действия:
1. Склонируйте репозиторий 
   ```
    https://github.com/Konst-Pav/python-project-52
   ```
2. Чтобы настроить среду для проекта, вам необходимо определить переменные среды в файле .env:
   ```
   SECRET_KEY=''
   DEBUG=False (либо True для режима отладки)
   DATABASE_URL='' (ссылку на базу данных)
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
