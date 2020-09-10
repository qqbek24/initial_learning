#****_Pyramid
#****_Autor: Jakub Koziorowski

import string

number = int(input("Input a number: "))
spaces = 2*number-2
for x in range(0, number):
    for y in range(0, spaces):
        print(end=" ")
    spaces = spaces-1
    for y in range(0, x+1):
        print(string.ascii_lowercase[y], end="")
    for y in range(x, 0, -1):
        print(string.ascii_lowercase[y-1], end="")
    print("\n")
