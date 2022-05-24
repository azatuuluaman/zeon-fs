import os

command = str(input('Enter the command for file (create , remove , dirname, find) : '))
if command == 'create':
    file_1 = str(input('Enter a new name for file: '))
    text_file = open(file_1, 'w')
    print('File', file_1, 'created!')

elif command == 'remove':
    file_2 = str(input('Enter file name to remove: '))
    os.remove(file_2)
    print('File', file_2, 'removed!')

elif command == 'dirname':
    print("All files:", os.listdir())

elif command == 'find':
    file_3 = str(input('Enter a file name for find: '))
    os.system(f"find {file_3}")




