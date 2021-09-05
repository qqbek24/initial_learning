#****_working with files - in Makbet
#****_Autor: Jakub Koziorowski

# TODO: check and clean the print section

f = open("Makbet.txt")
try:
    data = f.read()
finally:
    f.close()

#####instead use:

with open("Makbet.txt") as f:
    data = f.read()
    data.replace(",", ""). \
        replace(".", ""). \
        replace(":", ""). \
        replace(";", ""). \
        replace("'", ""). \
        replace("?", ""). \
        replace("|", "")
    data=data.upper()
    x = []
    x = data.splitlines()
    y = []
    y = data.split()
    Slownik = {}

    """for Slowo in y:
        z = y.count(Slowo)
        Slownik[Slowo] = z"""


#print(type(data))
print("Makbet ma ", len(x), " lini tekstu")
print("Makbet ma ", len(y), " slow")
#print("Makbet ma ", Slownik, " slow")
