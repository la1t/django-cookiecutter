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


def main():
    init_repo()
    print(SUCCESS + 'Project initialized, keep up the good work!' + TERMINATOR)


if __name__ == '__main__':
    main()
