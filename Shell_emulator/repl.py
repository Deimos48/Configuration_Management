from commands import builtIn

COMMANDS = {
    "exit": builtIn.cmd_exit,
    "help": builtIn.cmd_help,
    "echo": builtIn.cmd_echo,

}

def handle_command(cmd: str) -> bool:
    parts = cmd.split()
    name, args = parts[0], parts[1:]

    if (name in COMMANDS):
        return COMMANDS[name](args)
    else:
        print(f"[DEBUG] Команда {name} не поддерживается")
        return True


def repl():
    print("Мини-оболочка.\nВведите 'help' для справки, 'exit' для выхода")
    while True:
        try:
            cmd = input(">>> ").strip()
            if not cmd:
                continue
            if not handle_command(cmd):
                break
        except (KeyboardInterrupt, EOFError):
            print("\nВыход из эмулятора")
            break
