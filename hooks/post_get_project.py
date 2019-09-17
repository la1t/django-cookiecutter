import shutil

TERMINATOR = "\x1b[0m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def remove_accounts_app():
    accounts_path = '{{ cookiecutter.project_slug }}'
    shutil.removetree(accounts_path)


def main():
    if '{{ cookiecutter.use_custom_user_model }}' == 'n':
        remove_accounts_app()
    print(SUCCESS + 'Project initialized, keep up the good work!' + TERMINATOR)


if __name__ == '__main__':
    main()
