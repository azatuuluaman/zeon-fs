# from main import this_link

# Первое задание: тест на ссылку статичное
# def test_link1():
#     assert link1() == ['/hme/umar/Desktop/Amaka/Blog1/neolabs.py']


# Второе задание: тест на ссылку динамичное
# def test_this_link():
#     assert this_link() == '/home/umar/Desktop/Amaka/Blog1/1_test_test'

# Третье задание: возведение в степень.
# from main import number_degree
# from math import
#
#
# def test_number_degree():
#     assert number_degree(3) == x


# import sys
# script, command, *args = sys.argv
#
# if command == "init":
#     print("init fs")
#     if os.path.isdir("./zeon_fs"):
#         print("if folder is exits then nothing")
#     else:
#         print("else execute command mkdir zeon_fs")
# elif command == "add":
#     print(f"add file to fs: {args[0]}")
#



from main import *


# def test_parse_input():
#     arguments = []
#     assert parse_input(arguments) == None
#
#     arguments = ["helper.py"]
#     assert parse_input(arguments) == None
#
#     arguments = ["helper.py", "init"]
#     expected = ["init"]
#     actual = parse_input(arguments)
#     assert expected == actual
#
#     arguments = ["helper.py", "add",  "file.txt"]
#     expected = ["add",  "file.txt"]
#     actual = parse_input(arguments)
#     assert expected == actual


# command_list = ["init", "add", "del", "list", "get"]
#
#
# def parse_input(arguments):
#     if len(arguments) == 0:
#         return None
#
#     file_name, *args = arguments
#     match len(args):
#         case 1:
#             command = args[0]
#             return command
#         case 2:
#             command, argument = args
#             return [command, argument]
#         case _:
#             return None


# if name == 'main':
#     result = parse_input(sys.argv)
#     print(result)




    # if not x:
    #     print("Wrong arguments")

# if command == "init":
#     print("init fs")
#     if os.path.isdir("./zeon_fs"):
#         print("if folder is exits then nothing")
#     else:
#         print("else execute command mkdir zeon_fs")
# elif command == "add":
#     print(f"add file to fs: {args[0]}")