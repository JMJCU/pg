def my_range_while(start,stop, step=1):
    if step == 0:
       return print("Nemůže být nula.")

    vysledek = []
    while (start > stop if step < 0 else start < stop):
        vysledek.append(start)
        start += step
    return vysledek

def my_enumerate_for(iterable, start=0):
    vysledek = []
    for cislo in range(len(iterable)):
        vysledek.append((cislo + start, iterable[cislo]))
    return vysledek

def my_enumerate_while(iterable, start=0):
    vysledek = []
    cislo = 0
    while cislo < len(iterable):
        vysledek.append((cislo + start, iterable[cislo]))
        cislo += 1
    return vysledek

def my_zip(*iterables):
    vysledek = []
    for cislo in range(len(iterables[0])):
        # ntice z kazdeho implementovaneho objektu
        vysledek.append(tuple(iterable[cislo] for iterable in iterables))
    return vysledek


if __name__ == "__main__":
    print(list(range(1,10,2)))
    print(my_range_while(1,10,2))

    print(my_enumerate_for(["aaaa", "bbbb", "cccc"], start=1))
    print(list(enumerate(["aaaa", "bbbb", "cccc"], start=1)))
    print(my_enumerate_while(["aaaa", "bbbb", "cccc"], start=1))


    jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"]
    vek = [30, 20, 24, 18, 27]
    vaha = [50, 80, 90, 55, 67]

    print(list(zip(jmena, vek, vaha)))
    
    vysledek = my_zip(jmena, vek, vaha)
    print(vysledek)

    for jmeno, vek, vaha in vysledek:
        print(f"{jmeno} je {vek} let a vazi {vaha} kg")
