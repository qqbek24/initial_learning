# ****_The Harris Benedict Equation
# ****_Autor: Jakub Koziorowski

# TODO: change to function

'''
determines your total daily energy expenditure (calories).
The BMR formula uses the variables of height,
weight, age and gender to calculate the Basal Metabolic Rate (BMR).
'''

masa = float(input("Podaj swoja mase ciala [kg]: "))
wzrost = int(input("Podaj swoj wzrost [cm]: "))
wiek = int(input("Podaj swoj wiek: "))
plec = input("Podaj plec (m= men / w= women): ")

if plec == "m" or plec == "M":
    HB = 66.47 + (13.7*masa) + (5.0*wzrost) - (6.76*wiek)
    print("Mezczyzna: 66.47 + (13.7*Masa) + (5.0*Wzrost) - (6.76*Wiek) = \n", HB)
elif plec == "w" or plec == "W":
    HB = 655.1 + (9.567*masa) + (1.85*wzrost) - (4.68*wiek)
    print("Kobieta: 655.1 + (9.567*Masa) + (1.85*Wzrost) - (4.68*Wiek) = \n", HB)
else:
    print("Inna plec")
