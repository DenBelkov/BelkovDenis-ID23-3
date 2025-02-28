import os
import shutil
from config import directory

class TotalCommander:
    def __init__(self):
        self.default_dir = directory
        self.current_directory = directory

    def help(self):
        h = ['0: Выйти из менеджера',
             '1: Создать директорию ____ (mkdir)',
             '2: Удалить директорию ____ (rmdir)',
             '3: Сменить директорию (cd)',
             '4: Создать файл ____ (createf)',
             '5: Записать в файл ____ *текст* (writef)',
             '6: Прочитать файл ____ (readf)',
             '7: Удалить файл ____ (removef)',
             '8: Копировать файл ____ в *путь* (copyf)',
             '9: Переместить файл ____ в *путь* (movef)',
             '10: Переименовать файл ____ в ____ (renamef)',
             '11: Вывести все файлы в папке (ls)']
        for el in h: print(el)
    def change_directory(self, path):
        if path == '..':
            if self.current_directory == self.default_dir:
                return ("Нельзя выходить за пределы рабочей директории")
            else:
                self.current_directory =\
                    os.path.dirname(self.current_directory)
                return f"Перешли в директорию: {self.current_directory}"
        new_path = os.path.join(self.current_directory, path)
        print(new_path)
        if self.default_dir not in new_path:
                return ("Нельзя выходить за пределы рабочей директории")
        if os.path.isdir(new_path):
            self.current_directory = new_path
            return f"Перешли в директорию: {self.current_directory}"
        return "Директория не найдена."

    def list_files(self):
        return os.listdir(self.current_directory)

    def create_directory(self, name):
        os.makedirs(os.path.join(self.current_directory, name), exist_ok=True)
        return f"Создана директория: {name}"

    def remove_directory(self, name):
        path = os.path.join(self.current_directory, name)
        if os.path.isdir(path):
            os.rmdir(path)
            return f"Удалена директория: {name}"
        return "Директория не найдена."

    def create_file(self, name):
        with open(os.path.join(self.current_directory, name), 'w') as f:
            f.write('')
        return f"Создан файл: {name}"

    def read_file(self, name):
        path = os.path.join(self.current_directory, name)
        if os.path.isfile(path):
            with open(path, 'r') as f:
                return f.read()
        return "Файл не найден."

    def write_file(self, name, content):
        path = os.path.join(self.current_directory, name)
        if os.path.isfile(path):
            with open(path, 'a') as f:
                f.write(content)
            return f"Записано в файл: {name}"
        return "Файл не найден."

    def remove_file(self, name):
        path = os.path.join(self.current_directory, name)
        if os.path.isfile(path):
            os.remove(path)
            return f"Удален файл: {name}"
        return "Файл не найден."

    def copy_file(self, src, dest):
        src_path = os.path.join(self.current_directory, src)
        dest_path = os.path.join(self.current_directory, dest)
        if self.default_dir not in dest_path:
                return ("Нельзя выходить за пределы рабочей директории")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            return f"Скопирован файл: {src} в {dest}"
        return "Файл не найден."

    def move_file(self, src, dest):
        src_path = os.path.join(self.current_directory, src)
        dest_path = os.path.join(self.current_directory, dest)
        if self.default_dir not in dest_path:
                return ("Нельзя выходить за пределы рабочей директории")
        if os.path.isfile(src_path):
            shutil.move(src_path, dest_path)
            return f"Перемещен файл: {src} в {dest}"
        return "Файл не найден."

    def rename_file(self, old_name, new_name):
        old_path = os.path.join(self.current_directory, old_name)
        new_path = os.path.join(self.current_directory, new_name)
        if os.path.isfile(old_path):
            os.rename(old_path, new_path)
            return f"Переименован файл: {old_name} в {new_name}"
        return "Файл не найден."


def main():
    fm = TotalCommander()
    print("Добро пожаловать в файловый менеджер!")
    print("Для просмотра списка комманд введите help")
    while True:

        command = input(f"{fm.current_directory}> ").strip().split()
        if not command:
            continue

        cmd = command[0]
        if cmd == "help":
            fm.help()

        if cmd == "0" or cmd == 'exit':
            break

        elif cmd == "1" or cmd == 'mkdir':
            if len(command) > 1:
                print(fm.create_directory(command[1]))
            else:
                print("Вы не указали имя директории.")

        elif cmd == '2' or cmd == 'rmdir':
            if len(command) > 1:
                print(fm.remove_directory(command[1]))
            else:
                print("Вы не указали имя директории.")

        elif cmd == "3" or cmd == 'cd':
            if len(command) > 1:
                print(fm.change_directory(command[1]))
            else:
                print("Вы не указали имя директории.")

        elif cmd == '4' or cmd == 'createf':
            if len(command) > 1:
                print(fm.create_file(command[1]))
            else:
                print("Вы не указали имя файла.")

        elif cmd == '5' or cmd == 'writef':
            if len(command) > 1:
                print(fm.write_file(command[1], ' '.join(command[2:])))
            else:
                print("Вы не указали имя файла.")

        elif cmd == '6' or cmd == 'readf':
            if len(command) > 1:
                print(fm.read_file(command[1]))
            else:
                print("Вы не указали имя файла.")

        elif cmd == '7' or cmd =='removef':
            if len(command) > 1:
                print(fm.remove_file(command[1]))
            else:
                print("Вы не указали имя файла.")

        elif cmd == '8' or cmd == 'copyf':
            if len(command) > 1:
                print(fm.copy_file(command[1], command[2]))
            else:
                print("Вы не указали имя файла и директории.")

        elif cmd == '9' or cmd == 'movef':
            if len(command) > 1:
                print(fm.move_file(command[1], command[2]))
            else:
                print("Вы не указали имя файла и директории.")

        elif cmd == '10' or cmd == 'renamef':
            if len(command) > 1:
                print(fm.rename_file(command[1], command[2]))
            else:
                print("Вы не указали старое и новое имя файла")

        elif cmd == "11" or cmd == 'ls':
            print(fm.list_files())

if __name__ == '__main__':
    main()