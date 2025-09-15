def cmd_exit(args: list[str]) -> bool:
    # Завершение работы эмулятора
    print("Выход из эмулятора")
    # Продолжать ввод?
    return False

def cmd_help(args: list[str]) -> bool:
    # Печать справки
    print("Доступные команды: help, exit, echo")
    return True

def cmd_echo(args: list[str]) -> bool:
    # Вывод текста
    print(" ".join(args))
    return True

def cmd_ls(args: list[str]) -> bool:
    # Вывод окружающих файлов (Заглушка)
    print("ls " + " ".join(args))
    return True

def cmd_cd(args: list[str]) -> bool:
    # Переход по файлам (Заглушка)
    print("cd " + " ".join(args))
    return True
