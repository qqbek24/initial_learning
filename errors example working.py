#****_error handling examples
#****_Autor: Jakub Koziorowski

while True:
    try:
        dane_wej = str(input("enter your zip-code XX-XXX: "))
        if not len(dane_wej) == 6:
            raise ValueError
        if dane_wej[2] != "-":
            raise ValueError
        if not (dane_wej[0:2] + dane_wej[3:]).isdecimal():
            raise ValueError

        print("its ok")
        print(dane_wej)
        break

    except ValueError:
        print("hej, nie moge zgadnac liczby")