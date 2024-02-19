import random

def wurfeln():
    return random.randint(1, 6)

def main():
    playerscore = 0
    compscore = 0

    print("1 um zu starten")
    selection = int(input())

    if selection == 1:
        for _ in range(6):
            input("Drücken Enter um zu starten")
            S1 = wurfeln()
            S2 = wurfeln()
            playerscore += S1
            compscore += S2
            print("Spieler 1 hat", S1)
            print("Spieler 2 hat", S2)

        print("Aktueller Punktestand S1", playerscore)
        print("Aktueller Punktestand S2", compscore)

        if playerscore > compscore:
            print("Sieger")
        elif playerscore < compscore:
            print("Verloren")
        else:
            print("Unentschieden")

    else:
        print("Das war keine 1! Das Spiel wird beendet.")

if __name__ == "__main__":
    main()
