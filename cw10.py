import math

print("Podstawowe liczydło - pierwiastek kwadratowy")
a = float(input("Podaj liczbę: \n"))

b = str(math.sqrt(a))
a = str(a)

numa, decimala = [int(part) for part in a.split('.')]
numb, decimalb = [int(part) for part in b.split('.')]


if decimalb == 0 and decimala == 0:
    print(f"Pierwiastek z {numa} = {numb}")

if decimalb != 0 and decimala == 0:
    print(f"Pierwiastek z {numa} = {b}")

if decimalb == 0 and decimala != 0:
    print(f"Pierwiastek z {a} = {numb}")

if decimalb != 0 and decimala != 0:
    print(f"Pierwiastek z {a} = {b}")
