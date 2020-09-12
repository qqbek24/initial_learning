#****_map examples
#****_Autor: Jakub Koziorowski

def dodawanie(n):
    return n+n

liczba = (1, 2, 3, 4)

wynik = map(dodawanie, liczba)
print(list(wynik))
