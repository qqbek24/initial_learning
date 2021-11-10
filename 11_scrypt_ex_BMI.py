# ****_BMI_Body_Mass_Index
# ****_Autor: Jakub Koziorowski

xMasa = float(input("Podaj swoja mase ciala [kg]: "))
xWzrost = float(input("Podaj swoj wzrost [m]: "))
xBMI = (xMasa/(xWzrost**2))

if xBMI < 18.5:
    print('Niedowaga')
elif 18.5 <= xBMI < 25:
    print('Norma')
elif 25 <= xBMI < 30:
    print('Nadwaga')
else:
    print('Otylosc')
