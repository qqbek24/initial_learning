#****_Purpose: String manipulation
#****_Autor: Jakub Koziorowski
def word_count(wybrany_text):
    """Function that counts words in text"""

    list = wybrany_text.split()
    print(list)#len(list))

wybrany_text='''Wieręchmy się odarli i botów nie mamy,
    Już, panie, od pół roka suchych dni czekamy!"
    Trwaliście dłużej, dzieci, już dotrwajcie mało,
    Aż by się na tych targach wżdy co uprzedało.
    I u mnieć silny defekt, wierę, na kalecie.
    I w mieściechmy po trosze winni, sami wiecie!"
    Ale nie dziw, iż słudzy i pan nic nie mają,
    Bo jaki pan, taki kram, równo dopijają!'''

word_count(wybrany_text)