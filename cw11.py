print("Oblicznie modulo")

a = int(input("Podaj pierwszą liczbę: \n"))
b = int(input("Podaj drugą liczbę: \n"))


def modulo(x, y):
    z = x % y
    return z


print(f"Modulo równa się {modulo(a, b)}")
