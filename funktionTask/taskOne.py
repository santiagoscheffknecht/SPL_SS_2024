import random

# Erstelle eine Funktion die 2 Zahlen addiert
def adNumber(x, y):
    return x + y



# Erstelle eine Funktion, die eine zufällige Zahl zwischen 100 und 200 zurückliefert
def randomNumber():
    return random.randint(100, 200)




# Erstelle eine Funktion, die ein Wort aus einem String Array zurückliefert
def randomWord(string_array):
    return random.choice(string_array)



x = 69
y = 420
sum = adNumber(x, y)
print(sum)

randomNumber = randomNumber()
print(randomNumber)

word = ["Gangster", "CL500", "Strassenbande", "Croco", "Yay"]
otherWord = randomWord(word)
print(otherWord)






