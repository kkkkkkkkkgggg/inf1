print("Proste liczydło - dodawanie")
a = float(input("Podaj pierwszą liczbę: \n"))
b = float(input("Podaj drugą liczbę: \n"))


def dodawanie(x, y):
    z = x+y
    return z


print(f"Podane liczby to: {a,b}")
print(f"{a}+{b}={dodawanie(a, b)}")
