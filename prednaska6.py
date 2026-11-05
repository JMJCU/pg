
import random
import time
import datetime
import sys

symboly = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎", "🍍"]

def hraci_automat():
    step = 0

    while True:
        step += 1
        vysledek = []

        for i in range(3):
            vysledek.append(random.choice(symboly))

        print(vysledek)

        if len(set(vysledek)) == 1:
            print("Vyhrál jsi!")
            print(f"Počet pokusů: {step}")
            break

if __name__ == "__main__":
    # ts = time.time()
    # hraci_automat()
    # print(f"Čas hry: { (time.time() - ts) * 1000 } milisekund")

    d = datetime.date.today()
    print(d)
    d += datetime.timedelta(days=7)
    print(d.strftime("%d. %m. %Y"))

    n = datetime.datetime.now()
    print(n)
    n += datetime.timedelta(seconds=3600)
    print(n.strftime("%H:%M:%S %d. %m. %Y"))

    print(sys.argv)
    if len(sys.argv) <= 1:
        print("Pouziti: {sys.argv[0]} <jmeno souboru>")
        sys.exit()
    print(f"operace se souborem: {sys.argv[1]}")