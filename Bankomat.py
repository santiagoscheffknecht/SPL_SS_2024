import random

print("Willkommen beim Bankautomaten!")
balance = random.randint(0, 100)
print("Ihr Kontostand beträgt " + str(balance) + "€")

isFinished = False
while not isFinished:
    print("3Bitte wählen Sie eine Option:")
    print("1. Einzahlen")
    print("2. Abheben")
    print("3. Kontostand")
    print("4. Beenden")

    selection = int(input("Auswahl: "))

    if selection == 1:
        amount = int(input("Geben Sie den Betrag ein, den Sie einzahlen möchten: "))
        balance += amount
        print("Einzahlung erfolgreich. Ihr neuer Kontostand beträgt " + str(balance) + "€")

    elif selection == 2:
        amount = int(input("Geben Sie den Betrag ein, den Sie abheben möchten: "))
        if amount <= balance:
            balance -= amount
            print("Abhebung erfolgreich. Ihr neuer Kontostand beträgt " + str(balance) + "€")
        else:
            print("Sie haben nicht genügend Guthaben auf Ihrem Konto.")

    elif selection == 3:
        print("Ihr Kontostand beträgt " + str(balance) + "€")

    elif selection == 4:
        print("Vielen Dank für die Nutzung unseres Bankautomaten. Auf Wiedersehen!")
        isFinished = True

    else:
        print("Ungültige Auswahl. Bitte wählen Sie eine der verfügbaren Optionen (1-4).")
