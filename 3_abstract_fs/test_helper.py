from helper import *

import os


def hepler_remove_dir(file_name):
    os.rmdir(file_name)


def helper_remove_file(file_name):
    os.remove(file_name)

def helper_restore_file(file_name):
    text_file = open(file_name)

def test_init():
    name = 'zeon_fs'
    expected = 'Created!'
    actual = init_fs(name)
    assert expected == actual
    hepler_remove_dir(f'tests/{name}')


def test_add_file():
    arguments = os.getcwd() + '/test_assests/testt.txt'
    expected = 'Added!'
    actual = add_file(arguments)
    assert expected == actual
    helper_remove_file('./tests/testt.txt')

def test_list_files():
    expected = ['helper.py']
    actual = list_files('')
    assert expected == actual
#
#
def test_delete_file():
    arguments = ['testt.py']
    expected = 'Deleted!'
    actual = del_file(arguments)
    assert expected == actual


def test_get_file():
    name = 'testt2.txt'
    path = os.getcwd() + '/testt.txt'
    assert get_file(name, path) == True
