# ****_working with files - in Makbet
# ****_Autor: Jakub Koziorowski

# TODO: check and clean the print section

f = open("Makbet.txt", "w")
try:
    data = f.read()
finally:
    f.close()

# instead use:

with open("Makbet.txt") as f:
    data = f.read()
    data.replace(",", ""). \
        replace(".", ""). \
        replace(":", ""). \
        replace(";", ""). \
        replace("'", ""). \
        replace("?", ""). \
        replace("|", "")
    data = data.upper()

    Slownik = {}
    words = data.split()

for word in words:
    if word in Slownik:
        Slownik[word] += 1
    else:
        Slownik[word] = 1
    

# print("Makbet ma ", Slownik.values(), " slow")
print("Makbet ma ", len(Slownik), " slow")
print("slowo wystepuje", Slownik.get("MACBETH"), "razy")

# czestosc = list(Slownik.values())
# czestosc.sort()
# print(czestosc[-10:])
