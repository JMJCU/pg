def add (a,b):
    c = a + b
    return c 

def mul(a,b,c):
    return a*b*c

def div(a,b):
    if b == 0:
        return("0")
    else:
        return a/b

def divnothingleft(a, b):
    if a % b == 0:
        return "Je dělitelné bezezbytku"
    else:
        return "Není dělitelné bezezbytku"


def divnothingleft3(a):
    b = 3
    return divnothingleft(a, b)

if __name__ == "__main__":
    print("Hello World!")
    x = add(1, 2)
    print(x)
    resmul = mul(5,6,7)
    print(resmul)
    resdiv = div(5,2)
    print(resdiv)
    resdivnothingleft = divnothingleft(7,2)
    print(resdivnothingleft)
    print(divnothingleft3(13))