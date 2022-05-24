import sys
from helper import commands

_, command, *args = sys.argv
arg = sys.argv[2]
try:
    arg2 = sys.argv[3]
except:
    arg2 = ''

if command in commands:
    print(arg, arg2)
    commands[command](arg, arg2)

else:
    print('Error epta')
