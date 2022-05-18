import shutil
import sys
import os


# логика функционала
def init_fs(args):
    """
    Программа должна создать директорию zeon_fs
    """
    os.mkdir('zeon_fs')
    print('Директория создалась')


# def add_file(path):
    # src = f"{path}"
    #
    # shutil.copyfile(src,
    #
    # print(args, 'add')


def del_file(args):
    os.remove(str(args))
    print(args, 'deleted')


def list_files(_):
    print(os.listdir())


def get_file():
    pass


commands = {
    "init": init_fs,
    "add": add_file,
    "del": del_file,
    "get": get_file,
    "list": list_files
}

