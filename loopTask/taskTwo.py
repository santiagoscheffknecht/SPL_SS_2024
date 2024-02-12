# Zähle die geraden Ziffern zwischen 1 und 1000 zusammen 
# - Tip: Starte den Loop bei 2 und erhöhe den Zählindex jeweils um 2
allNumbers = 0
for number in range(0, 1000, 2):
    
    allNumbers += number

print(allNumbers)

# in if version
allNumbers = 0
for number in range(0, 1000):
    if number % 2 == 0:
        allNumbers += number

print(allNumbers)
