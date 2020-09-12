#****_map examples
#****_Autor: Jakub Koziorowski

x = range(10)

wynik_x = map((lambda n: n*2), x)
wynik_y = map((lambda n: n*2+1), x)
wynik_z = map((lambda n: n**3), x)
wynik_k = map((lambda n: n), reversed(x))

print(list(wynik_x))
print(list(wynik_y))
print(list(wynik_z))
print(list(wynik_k))