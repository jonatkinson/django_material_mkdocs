# django_material_mkdocs

A Django wrapper application to provide authentication (powered by `django-allauth`) to an `mkdocs` project. By default this also includes `mkdocs-material`.

The original author was Arlei F. Farnetani Junior (farnetani@gmail.com)

## Installation

- Requires Python version `3.4` or `3.5` (or above).
- `mkdir myproject`
- `cd myproject`
- `pipenv shell`
- `pipenv install`
- `mkdocs build`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`
- Open `http://localhost:8000/docs/`
- Login with the created superuser.
- That's it, you're finished.

## Todo

- Add a 'logout' link to the navigation.
