print("Liczydło - dzielenie")

a = float(input("Podaj pierwszą liczbę: \n"))
b = float(input("Podaj drugą liczbę: \n"))


def dzielenie(x, y):
    z = x/y
    return z


print(f"a/b = {dzielenie(a, b)}")
