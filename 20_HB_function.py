#****_Purpose: Harris and Benedict
#****_Autor: Jakub Koziorowski
def Harris_Benedict(Masa,Wzrost,Wiek,Plec):
    '''Function that greet user according to sex'''

    xBMI=(Masa/(Wzrost**2))
    if Plec =="m" or Plec=="M":
        HB=66.47 + (13.7*Masa) + (5.0*Wzrost) - (6.76*Wiek)
        print ("Mezczyzna: 66.47 + (13.7*Masa) + (5.0*Wzrost) - (6.76*Wiek) = \n", HB)
        if xBMI<18.5:
            print('Niedowaga\n')
        elif xBMI>=18.5 and xBMI<25:
            print('Normal\n')
        elif xBMI>=25 and xBMI<30:
            print('Nadwaga\n')
        else:
            print('Otylosc\n')
    elif Plec =="w" or Plec=="W":
        HB=655.1 + (9.567*Masa) + (1.85*Wzrost) - (4.68*Wiek)
        print ("Kobieta: 655.1 + (9.567*Masa) + (1.85*Wzrost) - (4.68*Wiek) = \n", HB)
        if xBMI<18.5:
            print('Niedowaga\n')
        elif xBMI>=18.5 and xBMI<25:
            print('Normal\n')
        elif xBMI>=25 and xBMI<30:
            print('Nadwaga\n')
        else:
            print('Otylosc\n')
    else:
        print ("Inna plec\n")
    
Harris_Benedict(55,180,30,"m")
Harris_Benedict(95,189,36,"m")
Harris_Benedict(70,160,45,"w")
Harris_Benedict(80,175,55,"t")
