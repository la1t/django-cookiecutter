#!/bin/sh

set -o errexit

pip3 install -r requirements.txt

mkdir -p .cache/bare
cd .cache/bare

cookiecutter ../../ --no-input --overwrite-if-exists
cd my_awesome_project

pipenv install
pipenv run python manage.py check
