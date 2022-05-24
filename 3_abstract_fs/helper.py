import os
import shutil


def init_fs(args, *arg):
    os.mkdir(f'tests/{args}')
    return 'Created!'


def add_file(path, *asd):
    src = f"{path}"
    dst = "tests"
    shutil.copy(src,dst)
    return 'Added!'


def list_files(_, *args):
    print(os.listdir())


def del_file(args, *asd):
    # os.remove(str(args))
    print('deleted')


def get_file(name, path):
    print('get_file')


commands = {
    "init": init_fs,
    "add": add_file,
    "del": del_file,
    "get": get_file,
    "list": list_files
}
