import random
# Erstelle zwei Zufallszahl zwischen 0 und 100
randomNumberO = random.randint(0, 100)
randomNumberT = random.randint(0, 100)
# Wenn die erste Zahl kleiner ist als die zweite UND die erste Zahl kleiner ist als 50
if randomNumberO<randomNumberT and randomNumberO<50:
# dann gib aus "Zahl 1 ist kleiner als Zahl 2 und Mini"
		print("Zahl 1 ist kleiner als Zahl 2 und Mini")
# Wenn die erste Zahl kleiner ist als 30 oder die zweite Zahl kleiner ist als 30
if randomNumberO<30 or randomNumberT<30:
# dann gib aus "Eine der beiden ist kleiner als 30"
		print("Eine der beiden ist kleiner als 30")
# Wenn die erste Zahl kleiner ist als 50 UND die zweite Zahl ungleich 50 ist
if randomNumberO<50	and	randomNumberT != 50:
# dann gib aus "Erste Zahl klein, zweite kein 50iger"
		print("Erste Zahl klein, zweite kein 50iger")