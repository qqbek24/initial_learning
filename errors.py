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
            raise  ValueError

#    except ValueError:
#        print("hej, nie moge zgadnac liczby")
#        dane_wej = 0
#    except KeyboardInterrupt:
#        print("you typed ctrl+C")
#    else:
#        if len(str(dane_wej)) == 5:
#            dane_wej = str(dane_wej)
#            dane_wyj = (dane_wej[0:2] + "-" + dane_wej[2:])
        print("its ok")
        print(dane_wej)
        break
#        elif str(dane_wej[0]) == "0":
#            print("0 na poczatku")
#        else:
#            print("cos poszlo nie tak")
    except ValueError:
        print("hej, nie moge zgadnac liczby")