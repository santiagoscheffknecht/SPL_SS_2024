import random

# Erstelle eine Zufallszahl zwischen 0 und 100
randomNumber = random.randint(0, 100)

# Gib die Zufallszahl aus
print(randomNumber)

# Wenn die Zahl kleiner ist als 20, gib "Mini" aus
if randomNumber < 20:
    print("Mini")

# Wenn die Zahl zwischen 20 und 50 ist, gib "Medium" aus
if 20 <= randomNumber <= 50:
    print("Medium")

# Wenn die Zahl größer als 50 ist, gib "Large" aus
else:
    print("Large")
