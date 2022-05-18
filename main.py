import sys
from helper import commands


_, command, *args = sys.argv

# print(sys.argv)
# print(command)
# print(_)
# print(*args)

# выбор функционала
if command in commands:
    commands[command](args)

else:
    print('fignya')

