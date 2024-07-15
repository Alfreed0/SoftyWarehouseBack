import os
import re
import sys

# Carpetas que deseamos excluir (en este caso, "libraries" y "venv")
EXCLUDE_FOLDERS = ["libraries", "venv", "scripts", "inv_venv"]

# Lista de directorios y archivos prohibidos
IGNORE_LIST = [".git", "__pycache__", "output.py"]


def detect_illegal_prints(file_path):
    with open(file_path) as f:
        content = f.read()
        prints = [
            (m.start(0), m.end(0)) for m in re.finditer(r"print\(", content)
        ]
        for start, end in prints:
            prev_content = content[max(0, start - 200): start]
            if (
                "#" in prev_content.split("\n")[-1]
                or content[:start].count('"""') % 2
            ):
                continue
            prev_lines = prev_content.split("\n")[-2:]  # Las últimas 2 líneas
            if not any("ALLOW_COMMIT" in line for line in prev_lines):
                line_number = content[:start].count("\n") + 1
                return f"{file_path} {line_number}"


def main():
    errors_detected = False
    for root, dirs, files in os.walk(os.getcwd()):
        # Omitir las carpetas "libraries" y "venv" en la búsqueda
        for folder in EXCLUDE_FOLDERS:
            if folder in dirs:
                dirs.remove(folder)

        for file in files:
            file_path = os.path.join(root, file)
            if any(
                dir_name in file_path for dir_name in IGNORE_LIST
            ) or not file_path.endswith(".py"):
                continue
            error_message = detect_illegal_prints(file_path)
            if error_message:
                print(error_message)
                errors_detected = True

    if errors_detected:
        print("Commit denied.")
        sys.exit(1)

    print("All checks passed ------> OK.")
    sys.exit(0)


if __name__ == "__main__":
    main()
