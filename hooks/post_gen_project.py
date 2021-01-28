import os
import shutil

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def init_repo():
    os.system('git init')
    os.system('git add .')
    os.system('git commit -q -m "Initial commit"')
    os.system('pre-commit install')


def delete_drf_dirs():
    core_path = '{{ cookiecutter.project_slug }}/core'
    shutil.rmtree(core_path)
    swagger_path = '{{ cookiecutter.project_slug }}/swagger'
    shutil.rmtree(swagger_path)


def main():
    if '{{ cookiecutter.rest_framework }}' == 'n':
        delete_drf_dirs()
    init_repo()
    print(SUCCESS + 'Project initialized, keep up the good work!' + TERMINATOR)


if __name__ == '__main__':
    main()
