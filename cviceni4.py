def levensteinova_vzdalenost(dotaz1, dotaz2):
    leventein = 0
    length = min(len(dotaz1), len(dotaz2))
    for i in range(length):
        if dotaz1[i] != dotaz2[i]:
            leventein += 1
    leventein += abs(len(dotaz1) - len(dotaz2))
    return leventein

def jaccardova_vzdalenost_mnozin(mnozina1, mnozina2):

    mnozina1 = set(mnozina1)
    mnozina2 = set(mnozina2)

    prunik = mnozina1.intersection(mnozina2)
    sjednoceni = mnozina1.union(mnozina2)
    # Výpočet Jaccardova indexu
    jaccard_index = len(prunik) / len(sjednoceni)
    # Výpočet Jaccardovy vzdálenosti
    jaccard_distance = 1 - jaccard_index
    return jaccard_distance


def deduplikace_dotazu(dotazy):
    i = 0
    while i < len(dotazy):
        j = i + 1
        while j < len(dotazy):
            jaccard = jaccardova_vzdalenost_mnozin(dotazy[i]["serp"], dotazy[j]["serp"])
            levenstein = levensteinova_vzdalenost(dotazy[i]["dotaz"], dotazy[j]["dotaz"])
            if jaccard < 0.5 or levenstein <= 1:
                dotazy.pop(j)
            else:
                j += 1
        i += 1
    return dotazy


if __name__ == "__main__":

    dotaz1 = {
        "dotaz": "seznam",
        "serp": ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    }
    dotaz2 = {
        "dotaz": "seznamka",
        "serp": ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    }
    dotaz3 = {
        "dotaz": "sesnam",
        "serp": ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
    }
    dotaz4 = {
        "dotaz": "google",
        "serp": ["https://www.google.com", "https://maps.google.com", "https://www.gmail.com"]
    }
    print(deduplikace_dotazu([dotaz1, dotaz2, dotaz3, dotaz4]))