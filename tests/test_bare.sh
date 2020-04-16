#!/bin/sh

set -o errexit

mkdir -p .cache/bare
cd .cache/bare

cookiecutter ../../ --no-input --overwrite-if-exists
cd my_awesome_project

pipenv run python manage.py check

# Clean
cd ..
rm -rf my_awesome_project
