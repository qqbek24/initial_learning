# ****_gwiazdki
# ****_Autor: Jakub Koziorowski

Liczba = int(input("Podaj liczbe: "))

for x in range(Liczba + 1, 1, -1):
    if x <= Liczba + 1:
        print("*" * (x - 1))
for x in range(2, Liczba + 1):
    print("*" * x)
