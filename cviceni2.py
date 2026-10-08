def vynasob_xty_prvek(seznam, x, nasobek):
    if 0 <= x - 1 < len(seznam):
        seznam[x - 1] = seznam[x - 1] * nasobek
        
    return seznam

def spocitej_prumer(seznam):
    if len(seznam) == 0:
        return None
    return sum(seznam) / len(seznam)

def formatuj_text(student):
    return print(f"Student {student["jmeno"]} {student["prijmeni"]}, Vek: {student["vek"]}, Prumer: {round(spocitej_prumer(student["znamky"]))}")

if __name__ == "__main__":

    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 12,
        "znamky": [1,2,1,1,3,2]
    }



    seznam = vynasob_xty_prvek([1, 2, 3, 4, 5], 3, 10)
    print(seznam)

    prumer = spocitej_prumer(seznam)
    print(prumer)

    print(formatuj_text(student))
        

    #vek = int(input("zadej svuj vek: "))

    #if vek >= 21:
    #    print("Muzes pit v USA")
    #else:
    #    print("dej si colu")
        
    #print(f"za rok ti bude {vek + 1}")

    #seznam = [1,2,3, "ctyri", 5]
    #print(seznam)
    #seznam.append("ahoj")
    #print(seznam[2])

    #print(f"seznam ma {len(seznam)} prvku")