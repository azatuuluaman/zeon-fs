from helper import *

import os


def hepler_remove_dir(file_name):
    os.rmdir(file_name)


def helper_remove_file(file_name):
    os.remove(file_name)


def test_init():
    name = 'zeon_fs'
    expected = 'Created!'
    actual = init_fs(name)
    assert expected == actual
    hepler_remove_dir(f'tests/{name}')


def test_add_file():
    arguments = os.getcwd() + '/helper.py'
    expected = 'Added!'
    actual = add_file(arguments)
    assert expected == actual


def test_list_files():
    expected = ['helper.py']
    actual = list_files('')
    assert expected == actual


def test_delete_file():
    arguments = []
    expected = 'Not Found!'
    actual = del_file(arguments)
    assert expected == actual

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
