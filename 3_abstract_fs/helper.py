import os
import shutil


def init_fs(args, *arg):
    os.mkdir(f'tests/{args}')
    return 'Created!'


def add_file(path, *asd):
    src = ''.join(path)  # превращает лист в стринг
    dst = "tests"
    os.system(f'cp {src} ./tests')  # копирует src в tests
    return 'Added!'


def list_files(_, *args):
    print(os.listdir())
    return os.listdir(path='tests')


def del_file(args, *asd):
    os.remove(args[0])
    return 'Deleted!'


def get_file(name, path):
    try:
        with open(path, 'r') as file_1:
            with open(name, 'w') as file_2:
                for i in file_1.readlines():
                    file_2.writelines(i)
        return True
    except:
        return False


commands = {
    "init": init_fs,
    "add": add_file,
    "del": del_file,
    "get": get_file,
    "list": list_files
}
