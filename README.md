Django Cookiecutter
===================
[![Build Status](https://travis-ci.org/la1t/django-cookiecutter.svg?branch=master)](https://travis-ci.org/la1t/django-cookiecutter)

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), Cookiecutter Django is a framework for jumpstarting production-ready Django projects quickly

## Features

* 12-Factor base settings via [django-environ](https://github.com/joke2k/django-environ)
* Error logging with [Sentry](https://sentry.io/organizations/anatoly-gusev/issues/)
* Manage virtual environments with [Pipenv](https://github.com/pypa/pipenv)
* Base [Celery](https://github.com/celery/celery) configuration

## Usage

First, get Cookiecutter and Pipenv:

    $ pip install cookiecutter pipenv

Now run it against this repo:

    $ cookiecutter https://github.com/la1t/django-cookiecutter

You'll be prompted for some values. Provide them, then a Django project will be created for you.

Happy hacking!!!
