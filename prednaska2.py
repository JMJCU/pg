if __name__ == "__main__":

    seznam = [1,2,3,4]

    #x = input("Přidej prvek: ")
    #seznam.append(x)

    seznam.pop(1)

    print(seznam)
    print(seznam[0])
    seznam[0] = 10
    

    n_tice = (1,2,3,4)
    print(n_tice)

    slovnik = {"jmeno": "Vlada"}
    print("Cely slovnik", slovnik)
    print("Jmeno", slovnik["jmeno"])
    slovnik["jmeno"] = "Petr"
    slovnik["nestekpestykonino"] = True
    print("Cely slovnik", slovnik)


    uzivatele = [{"jmeno": "Vlada", "vek":25}, {"jmeno": "Petr", "vek": 20}]
    print(uzivatele[1]["jmeno"])

    mnozina = {1,2,3,4}
    print(mnozina)
    print("Obsahuje množina 1?", 1 in mnozina)
    mnozina.add(5)
    mnozina.add(5)
    mnozina.add(5)
    mnozina.add(5)
    print("mnozina obsahuje 5", 5 in mnozina)
    print("Mnozina", mnozina)

    a = [1,2,3]
    print("novy seznam", a)
    b = a
    print("druhy seznam", b)
    b.append(4)
    print("seznam a", a)
    print("seznam b", b)

    # odkazuje A na stejný objekt jako B
    print(a is b)

    print(abs(-5)) #absolutni hodnota
    print(len("python")) #delka
    print(min(1,5,3)) # nejnizsi
    print(max(1,5,3)) # nejvyssi

    jmeno = "Palice"
    vek = 69
    print(f"Ahoj, jsem {jmeno} a prijmeni Alice a je mi {vek} let.")

    dvajmeno = input("Zadej svoje jmeno:")
    dvavek = int(input("zadej svuj vek:"))
    dvavek += 1

    print(f"tvoje jmeno je {dvajmeno} a za rok ti bude {dvavek} let")
    