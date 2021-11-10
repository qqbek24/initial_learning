# ****_Purpose: Harris and Benedict
# ****_Autor: Jakub Koziorowski

def harris_benedict(masa, wzrost, wiek, plec):
    '''Function that greet user according to sex'''

    xBMI = (masa / (wzrost ** 2))
    if plec == "m" or plec == "M":
        HB = 66.47 + (13.7 * masa) + (5.0 * wzrost) - (6.76 * wiek)
        print("Mezczyzna: 66.47 + (13.7*masa) + (5.0*wzrost) - (6.76*wiek) = \n", HB)
        if xBMI < 18.5:
            print('Niedowaga\n')
        elif 18.5 <= xBMI < 25:
            print('Normal\n')
        elif 25 <= xBMI < 30:
            print('Nadwaga\n')
        else:
            print('Otylosc\n')
    elif plec == "w" or plec == "W":
        HB = 655.1 + (9.567 * masa) + (1.85 * wzrost) - (4.68 * wiek)
        print("Kobieta: 655.1 + (9.567*masa) + (1.85*wzrost) - (4.68*wiek) = \n", HB)
        if xBMI < 18.5:
            print('Niedowaga\n')
        elif 18.5 <= xBMI < 25:
            print('Normal\n')
        elif 25 <= xBMI < 30:
            print('Nadwaga\n')
        else:
            print('Otylosc\n')
    else:
        print("Inna plec\n")


harris_benedict(55, 180, 30, "m")
harris_benedict(95, 189, 36, "m")
harris_benedict(70, 160, 45, "w")
harris_benedict(80, 175, 55, "t")
