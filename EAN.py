import shutil
import random
import pyfiglet
def generate_ean13():
    digits = [random.randint(0, 9) for _ in range(12)]
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 0:
            total += d
        else:
            total += d * 3
    check_digit = (10 - (total % 10)) % 10
    return ''.join(map(str, digits)) + str(check_digit)
print(pyfiglet.figlet_format("Wilkommen!"))
width = shutil.get_terminal_size().columns
print("-" * width)
while True:
    print(pyfiglet.figlet_format("Feature Auswählen:"))
    print("1: EAN Checker")
    print("2: EAN Generator")
    print("3: Rechner")
    print("-" * width)
    f = input("")
    print("~" * width)
    if f == "1":
        print("\033[33mEAN Checker\033[0m")
        num = input("\033[34mGib eine EAN ein: \033[0m")
        if num == "":
            print("\033[31mProgramm Beendet\033[0m")
            break
        if not num.isdigit(): 
            print("\033[31mBitte gib eine Nummer ein\033[0m")
        elif len(num) != 13:
            print("\033[31mEAN muss 13 Zeichen lang sein\nBitte Überprüfe deine Eingabe!!\033[0m")
        else:
            digits = [int(x) for x in num]
            check_digit = digits[-1]
            numbers = digits[:-1]
            numbers.reverse()
            total = 0
            for i, n in enumerate(numbers):
                if i % 2 == 0:
                    total += n * 3
                else:
                    total += n
            calc = (10 - (total % 10)) % 10
            if calc == check_digit:
                print("\033[32mGültig\n\033[0m")
            else:
                print("\033[31mUngültig\n\033[0m")
        print("-" * width)
    elif f == "2":
        print("\033[33mEAN Generator\033[0m")
        ean = generate_ean13()
        print("#" * width)
        print("\033[33mZufällige Mathematisch Gültige EAN:\033[0m")
        print("\n"+ ean)
        print("-" * width)
    elif f == "":
        print("\033[31mProgramm Beendet\033[0m")
        break
    elif f == "3":
        print("\033[36mRechner:")
        num1 = input("Erste Zahl: ")
        num2 = input("Zweite Zahl: ")
        op = input("Operation: +, -, *, /")
        if not num1.isdigit() or not num2.isdigit():
            print("Bitte Number eingeben!")
        num1 = float(num1)
        num2 = float(num2)
        if (op == "/" or op == "*" or op == "+" or op == "-"):
            if op == "+":
                print("Ergebnis:", num1 + num2)
            elif op == "-":
                print("Ergebnis:", num1 - num2)
            elif op == "*":
                print("Ergebnis:", num1 * num2)
            elif op == "/":
                if num2 == 0:
                    print("Kann nicht durch 0 Teilen")
                else:
                    print("Ergebnis:", num1/ num2)
            else:
                print("Ungültig")
    else:
        print("\033[31mUngültige Eingabe\033[0m")
        print("-" * width)