#****_Funkcje
#****_Autor: Jakub Koziorowski

def przywitaj (imie="Jan", plec="m"):
    if plec == "m":
        print ("Witaj drogi ", imie, "!")
    elif plec == "k":
        print ("Raczki caluje, droga ", imie, "!")
    else:
        print ("no to czesc")

        
przywitaj("Pawle","t")
przywitaj("Moniko","k")
przywitaj("Sebastian","m")
przywitaj()
