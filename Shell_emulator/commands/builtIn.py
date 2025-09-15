from vfs import VirtualFileSystem

vfs = VirtualFileSystem()

def cmd_exit(args: list[str]) -> bool:
    # Завершение работы эмулятора
    print("Выход из эмулятора")
    # Продолжать ввод?
    return False

def cmd_help(args: list[str]) -> bool:
    # Печать справки
    print("Доступные команды: help, exit, echo")
    return True

def cmd_ls(args: list[str]) -> bool:
    # Вывод окружающих файлов
    items = vfs.listdir()
    print("  ".join(items))
    return True

def cmd_cd(args: list[str]) -> bool:
    # Переход по файлам (Заглушка)
    if not args:
        print("cd: требуется аргумент")
        return True
    vfs.chdir(args[0])
    return True

def cmd_pwd(args: list[str]) -> bool:
    # Полный путь
    print(vfs.getcwd())
    return True
