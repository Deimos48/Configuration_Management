import getpass
import shlex
import socket

from commands import builtIn
from commands.builtIn import vfs

COMMANDS = {
    "exit": builtIn.cmd_exit,
    "help": builtIn.cmd_help,
    "ls": builtIn.cmd_ls,
    "cd":builtIn.cmd_cd,
    "pwd":builtIn.cmd_pwd,

}

def handle_command(cmd_line: str) -> bool:
    try:
        parts = shlex.split(cmd_line)
        if not parts:
            return True  # пустой ввод
        name, args = parts[0], parts[1:]
        if name in COMMANDS:
            return COMMANDS[name](args)
        else:
            print(f"Ошибка: неизвестная команда '{name}'")
            return True
    except ValueError as e:
        print(f"Ошибка парсинга команды: {e}")
        return True


def repl():
    print("Мини-оболочка. Введите 'help' для справки, 'exit' для выхода")
    username = getpass.getuser()
    hostname = socket.gethostname()

    while True:
        try:
            prompt = f"{username}@{hostname}:{vfs.getcwd()}~$ "
            cmd_line = input(prompt)
            if not handle_command(cmd_line):
                break
        except (KeyboardInterrupt, EOFError):
            print("\nВыход из эмулятора")
            break
