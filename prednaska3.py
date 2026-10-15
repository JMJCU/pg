def vypocet(*args, **kwargs):
    a = kwargs.get('a', 0)
    vysledek = a + 1
    print("funkce funguje")
    return vysledek

x = 10
x = x - 1

def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial(n - 1)

if __name__ == "__main__":
    print(vypocet(100, a=1, b=2, c=3))
    print(faktorial(5))