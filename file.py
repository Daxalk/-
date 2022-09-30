import os
import shutil
import file_config


def create_folder():
    print('Введите название папки')
    folder_name = input()
    os.mkdir(folder_name)
    print('Папка "{}" успешно создана'.format(folder_name))


def delete_folder():
    print('Введите название папки')
    folder_name = input()
    os.rmdir(folder_name)
    print('Папка "{}" удалена удалена'.format(folder_name))


def change_directory():
    print('Введите название папки, в которую хотите попасть или напишите return, чтобы выйти из текущей директории')
    print('Вы находитесь в {}'.format(os.getcwd()))
    folder_name = input()
    if folder_name == 'return':
            path = str(os.getcwd()).split('\\')
            new_path = ''
            for folders in range(len(path)-1):
                new_path += path[folders] + '\\'

    elif os.path.exists(folder_name):
        os.chdir(folder_name)
    else:
        print('Такой папки нет')

    print('Вы находитесь в {}'.format(os.getcwd()))


def create_file():
    print('Введите название файла')
    file_name = input()
    file = open(file_name, 'w+')
    file.close()
    print('Файл "{}" успешно создан'.format(file_name))


def write_in_file():
    print('Введите название файла')
    file_name = input()
    if os.path.exists(file_name):
        file = open(file_name, 'w+')
        print('Введите текст для файла')
        text = input()
        file.write(text)
        file.close()
        print('Текст записан в файл "{}"'.format(file_name))
    else:
        print('Файла "{}" нет'.format(file_name))


def read_file():
    print('Введите название файла')
    file_name = input()
    if os.path.exists(file_name):
        file = open(file_name, 'r')
        for line in file:
            print(line)
        file.close()
    else:
        print('Файла "{}" нет'.format(file_name))


def delete_file():
    print('Введите название файла')
    file_name = input()
    if os.path.exists(file_name):
        os.remove(file_name)
        print('Файл "{}" успешно удален'.format(file_name))
    else:
        print('Файла "{}" нет'.format(file_name))



def copy_file():
    print('Введите название файла')
    file_name = input()
    print('Введите путь для файла')
    file_path = input()
    if os.access(file_path, os.X_OK):
        if os.path.exists(file_name):
            shutil.copy(file_name, file_path)
            print('Файл {} успешно скопирован в {}'.format(file_name, file_path))
        else:
            print('Файла "{}" нет'.format(file_name))


def moving_files():
    print('Введите название файла')
    file_name = input()
    print('Введите путь для файла')
    file_path = input()
    if os.access(file_path, os.X_OK ):
        if os.path.exists(file_name):
            shutil.move(file_name, file_path)
            print('Файл {} успешно перемещен в {}'.format(file_name, file_path))
        else:
            print('Файла "{}" нет'.format(file_name))


def rename_file():
    print('Введите название файла')
    file_name = input()
    if os.path.exists(file_name):
        print('Введите новое название файла')
        new_file_name = input()
        os.rename(file_name, new_file_name)
        print('Файл "{}" успешно переименован в "{}"'.format(file_name, new_file_name))
    else:
        print('Файла "{}" нет'.format(file_name))


main_directory = os.chdir(file_config.root_direction)
while True:
    print(
        'Введите "1", чтобы создать папку\nВведите "2", чтобы удалить папку\nВведите "3", чтобы переместиться между папками\nВведите "4", чтобы создать файл\nВведите "5", чтобы записать текст в файл\nВведите "6", чтобы просмотреть содержимое файла\nВведите "7", чтобы удалить файл\nВведите "8", чтобы копировать файл в другую папку\nВведите "9", чтобы переместить файл в другую папку\nВведите "10", чтобы переименовать файл')

    command = int(input())

    if command == 1:
        create_folder()
    elif command == 2:
        delete_folder()
    elif command == 3:
        change_directory()
    elif command == 4:
        create_file()
    elif command == 5:
        write_in_file()
    elif command == 6:
        read_file()
    elif command == 7:
        delete_file()
    elif command == 8:
        copy_file()
    elif command == 9:
        moving_files()
    elif command == 10:
        rename_file()
