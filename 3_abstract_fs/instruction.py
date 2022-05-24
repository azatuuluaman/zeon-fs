# Моделирование абстрактной файловой системы 23.05.22

# Директория
# Файл
#     Название файла

# Декомпозиция абстрактной файловой системы 23.05.22

# Команда для инициализации корневого каталога
    # Ввод команды и названия директории
    # Создание директории

# Команда для добавления файла
    # Ввод команды и адреса откуда нужно скопировать
    # Придаем переменной адрес копируемого файла
    # Придаем переменной адрес куда нужно скопировать
    # Копируем

# Команда для удаления файла
    # Ввод команды и названия файла
    # Удаление файла

# Команда для получения списка файлов
    # Ввод команды
    # Вывод списка файлов

# Команда получения файла
    # Ввод команды, названия нового файла и адрес копируемого файла
    # Открытие копируемого файла
    # Открытие пустого файла с введенным названием
    # Перенос данных с копируемого файла в новый файл


#Декомпозиция:
    # dir_name = zeon_sf
    #
    # init_fs(dir_name: str) -> None:
    #     create directory(dir_name)
    # add_file(file_name:str) -> None:
    #     if not check_file(dir_path+file_name)
    #     else copy file in directory to dir_name and save that file with file_name name
    # delete_file(file_name: str) -> None:
    #     if not check_file(dir_path+file_name)
    #     else delete file in dir_name
    # get_file(file_name: str, file_path: str) -> None:
    #     if not check_file(dir_path+file_name)
    #     else create file - file_name
    # list_file(directory_path: str) -> None:
    #     return file list in directory_path
    #
    #
    # check_file(path: str) -> bool:
    #     if file not exists in path
    #         print(”File not exists”)
    #         return False
    #     return True

