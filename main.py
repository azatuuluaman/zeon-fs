import sys
from helper import commands


_, command, *args = sys.argv

# print(sys.argv)
# print(command)
# print(_)
# print(*args)

# выбор функционала
try:
    arg2 = sys.argv[2]
except:
    arg2 = ''


if command in commands:

    commands[command](args, arg2)

else:
    print('fignya')

