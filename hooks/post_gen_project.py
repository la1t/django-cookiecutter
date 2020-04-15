import os
import shutil

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def remove_accounts_app():
    accounts_path = '{{ cookiecutter.project_slug }}/users'
    shutil.rmtree(accounts_path)


def create_virtualenv(version):
    os.system('pipenv --python %s' % version)


def install_dependencies():
    os.system('pipenv install')


def init_repo():
    os.system('git init')
    os.system('git add .')
    os.system('git commit -q -m "Initial commit"')


def main():
    if '{{ cookiecutter.use_custom_user_model }}' == 'n':
        remove_accounts_app()
    
    print(INFO + 'Create virtual environment' + TERMINATOR)
    create_virtualenv('{{ cookiecutter.python_version }}')

    print(INFO + 'Install dependencies' + TERMINATOR)
    install_dependencies()

    init_repo()
    
    print(SUCCESS + 'Project initialized, keep up the good work!' + TERMINATOR)


if __name__ == '__main__':
    main()
