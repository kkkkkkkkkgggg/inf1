print("Liczydło - dzielenie lepsze")

a = float(input("Podaj pierwszą liczbę: \n"))
b = float(input("Podaj drugą liczbę: \n"))


def dzielenielepsze(x, y):
    z = x//y
    return z


print(f"a//b = {dzielenielepsze(a, b)}")
