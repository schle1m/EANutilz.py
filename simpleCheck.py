import shutil
width = shutil.get_terminal_size(fallback=(80, 24)).columns

while True:
    print("-" * width)
    print("EAN Checker")
    num = input("Gib eine EAN ein: ")
    if num == "":
        print("Programm Beendet")
        break
    if not num.isdigit():
        print("Bitte gib eine Nummer ein")
    elif len(num) != 13:
        print("EAN muss 13 Zeichen lang sein")
    else:
        digits = [int(x) for x in num]
        check_digit = digits[-1]
        numbers = digits[:-1]
        numbers.reverse()
        total = 0
        for i, n in enumerate(numbers):
            total += n * 3 if i % 2 == 0 else n
        calc = (10 - (total % 10)) % 10
        print("Gültig" if calc == check_digit else "Ungültig")
    print("-" * width)