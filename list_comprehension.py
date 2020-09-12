#****_list comprehension
#****_Autor: Jakub Koziorowski

x = [i for i in range(10) if not i%2]
y = [i for i in range(10) if i%2]
z = [i**3 for i in range(10)]
k = [i for i in reversed(range(10))]

print("Liczby parzyste", x)
print("Liczby nieparzyste", y)
print("szescian", z)
print("Odwrotne", k)