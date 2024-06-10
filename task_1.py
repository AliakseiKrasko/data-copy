def copy_line(source_file, target_file, line_number):
    try:
        with open(source_file, 'r') as source:
            lines = source.readlines()
            if 1 <= line_number <= len(lines):
                line_to_copy = lines[line_number - 1]
                with open(target_file, 'a') as target:
                    target.write(line_to_copy)
                print("Строка успешно скопирована.")
            else:
                print("Неверный номер строки.")
    except FileNotFoundError:
        print("Один из файлов не найден.")

# Пример использования:
source_file = 'source.txt'
target_file = 'target.txt'
line_number = int(input("Введите номер строки для копирования: "))
copy_line(source_file, target_file, line_number)