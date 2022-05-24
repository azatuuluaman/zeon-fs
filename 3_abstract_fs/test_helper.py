from helper import *

import os


# Для проверки команды которую мы вводим. Продолжу как разберу код.
# def check_commands():
#     arguments = ['helper.py', 'add', 'test_resources/test1/txt']
#     expected = 'Satisfield commands!'
#     actual = check_commands(arguments)
#     assert expected == actual
#
#     arguments = ['helper.py', 'add']
#     expected = 'You forgot to add one more argument!'
#     actual = check_commands(arguments)
#     assert expected == actual
#
#     arguments = ['helper.py', 'list']
#     expected = 'Satisfield commands!'
#     actual = check_commands(arguments)
#     assert expected == actual
#
#     arguments = ['helper.py', 'get', 'file_name']
#     expected = 'Extra uneedable arguments for' \
#                '"list" command'
#     actual = check_commands(arguments)
#     assert expected == actual
#
#     arguments = ['helper.py', 'get', 'text.txt', 'test_resources/test2.txt']
#     expected = 'You forgot to add one more argument!'
#     actual = check_commands(arguments)
#     assert expected == actual
#
#
# def hepler_remove_added_file(file_name):
#     os.remove(file_name)
#
#
# def helper_add_removed_file(file_name):
#     os.system(f'touch{file_name}')
def hepler_remove_dir(file_name):
    os.rmdir(file_name)


def test_init():
    # arguments = ['zeon_fs']
    # expected = 'Already exists'  # уже существует
    # actual = init(arguments)
    # assert expected == actual

    name = 'zeon_fs'
    expected = 'Created!'
    actual = init_fs(name)
    assert expected == actual
    hepler_remove_dir(f'tests/{name}')


# def test_list_files():
#     expected = ['__pycache__', 'helper.py', 'helper.py',
#                 'structure.txt', 'test_assets',
#                 'test_commands.py', 'test_main.py',
#                 'test_resources']
#     actual = list_files()
#     assert expected == actual


def test_add_file():
    arguments = 'helper.py'
    expected = 'Added!'
    actual = add_file(arguments)
    assert expected == actual


    # arguments = ['test_resources/non_existing_file.txt']
    # expected = 'Incorect_path!'
    # actual = add_file(arguments)
    # assert expected == actual
    #
    # arguments = ['test_resources/test_existin_file.txt']
    # expected = 'Already exists!'
    # actual = add_file(arguments)
    # assert expected == actual
#
#
# def test_delete_file():
#     arguments = ['zeon_fs/non_existing_file.txt']
#     expected = 'Not Found!'
#     actual = del_file(arguments)
#     assert expected == actual
#
#
#
#
# arguments = ['zeon_fs/non_existing_file.txt']
# expected = 'Not Found!'
# actual = del_file(arguments)
# assert expected == actual
#
#
# def test_get_file():
#     arg1, arg2 = ['new_file_name.txt',
#                   'test_resources/test5.txt']
#     expected = 'Content successfully copied!'
#     actual = get_file(arg1, arg2)
#     assert expected == actual
#
#     arg1, arg2 = ['new_file_name.txt',
#                   'test_resources/test5.txt']
#     expected = 'This file already exists!'
#     actual = get_file(arg1, arg2)
#     assert expected == actual
