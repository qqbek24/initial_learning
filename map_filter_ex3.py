#****_map filter examples
#****_validate brackets (), {}, []
#****_Autor: Jakub Koziorowski

# Zwaliduj poprawnośc nawiasów.
# Chodzi o nawiasy : (), {}, []
# Dane wejścia - łańcuch znaków
# Chodzi o implementacji funkcji;
# Wynik działania funkcji będzie True jeżeli nawiasy są poprawne
# False w przeciwnym wypadku
# Każdy otwarty nawias - musi być zamknięty
# () - True
# ({[[]])} - True
# (XX)YY{[zzzzzz}jjdf]
# )( - False
# ] () [ - False
def check_parenthesis(insert_char):
    d = {"{": 0, "(": 0, "[": 0}
    for i in insert_char:
        if i in d.keys():
            d[i] += 1
        elif i == "}":
            d["{"] -= 1
        elif i == ")":
            d["("] -= 1
        elif i == "]":
            d["["] -= 1
        if d["{"] < 0 or d["("] < 0 or d["["] < 0:
            return False
    if d["{"] == 0 & d["("] == 0 & d["["] == 0:
        return True
    else:
        return False

print(check_parenthesis("(())"))
print(check_parenthesis("}{{{}}}"))

