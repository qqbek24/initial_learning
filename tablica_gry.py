# ****_Simple Game Board
# ****_Autor: Jakub Koziorowski & Kacper Kalamat

number_columns = int(input("Podaj liczbe kolumn: "))
number_rows = int(input("Podaj liczbe wierszy: "))


def print_game_board(number_rows, number_columns, shape="*"):
    '''funkcja sluzy do rysowania planszy'''
    print_header(number_columns)
    print_rows(number_columns, number_rows, shape)


def print_rows(number_columns, number_rows, shape):
    print("\t " + shape * (number_columns * 2) + shape)
    for x in range(0, number_rows):
        row_nr = str(x + 1)
        print(row_nr + "\t " + (shape + " ") * number_columns + shape)
        print("\t " + shape * (number_columns * 2) + shape)


def print_header(number_columns):
    print("\n")
    header = " " * 5
    for j in range(number_columns):
        header += " " + str(j + 1)
    print(header)


print_game_board(number_rows, number_columns, "*")
