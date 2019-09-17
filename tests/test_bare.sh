#!/bin/sh

set -o errexit

pip install -r requirements.txt

mkdir -p .cache/bare
cd .cache/bare

cookiecutter ../../ --no-input --overwrite-if-exists
cd my_awesome_project

pipenv install
pipenv run python manage.py check
