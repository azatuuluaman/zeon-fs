import shutil
import sys
import os


# логика функционала
def init_fs(args, *arg):
    """
    Программа должна создать директорию zeon_fs
    """
    os.mkdir('zeon_fs')
    print('Директория создалась')

# ИСПРАВИТЬ РАСПОЛОЖЕНИЕ
def add_file(path, *sad):
    src = f"{path[0]}"
    dst = '.'
    shutil.copy(src,dst)
    print(path, 'add')


def del_file(args, *asd):
    os.remove(str(args))
    print(args, 'deleted')


def list_files(_, *args):
    print(os.listdir())


def get_file(name, path):
    try:
        with open(path, 'r') as file_1:
            with open(name, 'w') as file_2:
                for i in file_1.readlines():
                    file_2.writelines(i)
            print(file_2)
    except:
        print('SALAM_epta')



commands = {
    "init": init_fs,
    "add": add_file,
    "del": del_file,
    "get": get_file,
    "list": list_files
}

