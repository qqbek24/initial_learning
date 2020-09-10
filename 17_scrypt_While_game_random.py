#****_While, gra magic number
#****_Autor: Jakub Koziorowski

import random

magic_number=random.randint(0,10)
Liczba=int(input("zgadnij Magic Number: "))
Proba=1
while magic_number != Liczba:
    print ("gramy dalej")
    Liczba=int(input("zgadnij Magic Number: "))
    Proba+=1
    
print ("Wygrales, liczba tur:", Proba)
