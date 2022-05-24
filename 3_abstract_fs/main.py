import sys
from helper import commands

_, command, *args = sys.argv

try:
    arg2 = sys.argv[2]
except:
    arg2 = ''

if command in commands:

    commands[command](args, arg2)

else:
    print('Error epta')
