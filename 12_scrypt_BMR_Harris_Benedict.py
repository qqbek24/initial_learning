#****_The Harris Benedict Equation
#****_Autor: Jakub Koziorowski

# TODO: change to function

'''determines your total daily energy expenditure (calories).
The BMR formula uses the variables of height,
weight, age and gender to calculate the Basal Metabolic Rate (BMR).
'''

Masa = float(input("Podaj swoja mase ciala [kg]: "))
Wzrost = int(input("Podaj swoj wzrost [cm]: "))
Wiek = int(input("Podaj swoj wiek: "))
Plec = input("Podaj plec (m=men / w=women): ")

if Plec == "m" or Plec == "M":
    HB = 66.47 + (13.7*Masa) + (5.0*Wzrost) - (6.76*Wiek)
    print("Mezczyzna: 66.47 + (13.7*Masa) + (5.0*Wzrost) - (6.76*Wiek) = \n", HB)
elif Plec == "w" or Plec == "W":
    HB = 655.1 + (9.567*Masa) + (1.85*Wzrost) - (4.68*Wiek)
    print("Kobieta: 655.1 + (9.567*Masa) + (1.85*Wzrost) - (4.68*Wiek) = \n", HB)
else:
    print("Inna plec")
