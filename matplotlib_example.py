# ****_turtle
# ****_Autor: Jakub Koziorowski

import matplotlib.pyplot as plt
import math

"""x = [2, 5, 10, 7]
y = [1, 5, 3, 9]
plt.plot(x,y)
plt.ylabel("to jest oś y")
plt.xlabel("to jest oś x")

plt.show()"""

#sin i cos (od 01 do 10)
def sin_cos():
    x = []
    y_sin = []
    y_cos = []

    for i in range(1000):
        j = i / 50
        x.append(j)
        y_sin.append(math.sin(j))
        y_cos.append(math.cos(j))


    plt.plot(x, y_sin, 'r-')
    plt.plot(x, y_cos, 'b-')
    plt.ylabel("to jest oś y")
    plt.xlabel("to jest oś x")

    plt.show()

sin_cos()