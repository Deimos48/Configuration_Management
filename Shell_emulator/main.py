import argparse
import sys

from repl import repl, handle_command


def run_script(script_path: str) -> None:
    try:
        with open(script_path, "r", encoding="utf-8") as f:
            for line in f:
                cmd_line = line.strip()
                if not cmd_line:
                    continue
                print(f">>> {cmd_line}")  # показываем как будто ввёл пользователь
                ok = handle_command(cmd_line)
                if not ok:  # команда exit или ошибка
                    print("Сценарий прерван из-за ошибки/exit")
                    return
    except FileNotFoundError:
        print(f"Ошибка: не найден скрипт {script_path}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Эмулятор оболочки")
    parser.add_argument("--vfs", help="Путь к виртуальной файловой системе", required=False)
    parser.add_argument("--script", help="Путь к стартовому скрипту", required=False)

    args = parser.parse_args()

    # Отладочный вывод параметров
    print(f"[DEBUG] Параметры запуска:")
    print(f"  VFS: {args.vfs}")
    print(f"  Script: {args.script}")

    if args.script:
        run_script(args.script)
    else:
        repl()


if __name__ == "__main__":
    main()
