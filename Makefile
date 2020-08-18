test:
	sh ./tests/test_bare.sh

create_project:
	cd .cache/ && rm -rf * && cookiecutter ../
