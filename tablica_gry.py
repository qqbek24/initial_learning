#****_Simple Game Board
#****_Autor: Jakub Koziorowski & Kacper Kalamat

numberColumns=int(input("Podaj liczbe kolumn: "))
numberRows=int(input("Podaj liczbe wierszy: "))


def print_game_board(numberRows, numberColumns, shape="*"):
    '''funkcja sluzy do rysowania planszy
    '''
    print_header(numberColumns)
    print_rows(numberColumns, numberRows, shape)


def print_rows(numberColumns, numberRows, shape):
    print("\t " + shape * (numberColumns * 2) + shape)
    for x in range(0, numberRows):
        row_nr = str(x + 1)
        print(row_nr + "\t " + (shape + " ") * numberColumns + shape)
        print("\t " + shape * (numberColumns * 2) + shape)


def print_header(numberColumns):
    print("\n")
    header = " " * 5
    for j in range(numberColumns):
        header += " " + str(j + 1)
    print(header)


print_game_board(numberRows, numberColumns, "*")