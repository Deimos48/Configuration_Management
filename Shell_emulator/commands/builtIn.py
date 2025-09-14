def cmd_exit(args: list[str]) -> bool:
    # Завершение работы эмулятора
    print("Выход из эмулятора")
    # Продолжать ввод?
    return False

def cmd_help(args: list[str]) -> bool:
    # Печать справки
    print("Доступные команды: help, exit")
    return True

def cmd_echo(args: list[str]) -> bool:
    # Вывод текста
    print(" ".join(args))
    return True
