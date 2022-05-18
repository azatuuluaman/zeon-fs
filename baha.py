# import sys, os
# from pathlib import Path
#
#
# class Directory:
#     def __init__(self, path=None, file_system_name='file_system.txt', mode='create') -> None:
#         self.file_system_name = file_system_name
#         match mode:
#             case 'load':
#                 self.load()
#             case 'create':
#                 self.path = path
#
#     def create(self, filename: str) -> None:
#         filename = self.check_file_name(filename)
#         open(filename, 'w').close()
#         print(f'File was created! {self.path}\\{filename}')
#
#     def delete(self, filename: str) -> None:
#         if filename in os.listdir():
#             os.remove(filename)
#             print(f'File {filename} was deleted')
#         else:
#             print(f'File not found!')
#
#     def list(self) -> None:
#         for name in os.listdir():
#             print(name)
#
#     def check_file(self, filename: str) -> bool:
#         if filename in os.listdir():
#             print('File was found!')
#             return True
#         else:
#             print('File not found!')
#             return False
#
#     def check_file_name(self, filename: str) -> str:
#         if filename in os.listdir():
#             filename = f'{Path(filename).stem} - Копия.{Path(filename).suffix}'
#             return self.check_file_name(filename)
#         return filename
#
#     def put(self) -> None:
#         if self.check_file(self.file_system_name):
#             with open(self.file_system_name, 'r') as file:
#                 self.path = file.readline(0)
#         print('Directory not initialized!')
#
#     def save(self) -> None:
#         with open(self.file_system_name, 'w') as file:
#             file.write(self.path)
#         print(f'Initialized empty FileSystem in {self}')
#
#     def __str__(self) -> str:
#         return f'{self.path}'
#
#
# def main():
#     argv = sys.argv[1:]
#     match argv:
#         case 'init', *argv:
#             directory = Directory(path=os.getcwd())
#             directory.save()
#         case 'create', filename, *argv:
#             directory = Directory(mode='load')
#             directory.create(filename=filename)
#         case 'delete', filename, *argv:
#             directory = Directory(mode='load')
#             directory.delete(filename=filename)
#         case 'list', *argv:
#             directory = Directory(mode='load')
#             directory.dir()
#         case 'search', filename, *argv:
#             directory = Directory(mode='load')
#             directory.check_file(filename=filename)
#         case _:
#             print('Command not found!')
#
#
# if __name__ == '__main__':
#     main()

class Window:
    def __init__(self, x, y):
        self.square = x * y

class Room:
    def __init__(self, x,y,z):
        self.square = 2 * z * (x + y)
        self.wd = Window(x * 0.5, y * 0.7)

r = Room(2,4,3)

# print(type(r), r)
# print(type(r.square), r.square)
print(type(r.wd))

w = Window(2,1)
print(type(w))