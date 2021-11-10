# ****_map filter examples
# ****_validate brackets (), {}, []
# ****_Autor: Jakub Koziorowski

# Zwaliduj poprawność nawiasów.
# Chodzi o nawiasy: (), {}, []
# Dane wejscie- łąńcuch znaków
# Chodzi o implemenetacji funkcji;
# Wynik działania funkcji będzie True jeżeli nawiasy są poprawne
# False w przeciwnym wypadku
# Każdy otwarty nawias - musi zamknięty
# 1. () - True
# 2. ({[[]])} - True
# 3. (XX)YY{[zzzz}jjdf] - True
# 4. )( - False
# 5. ] () { - False


def parentis_validation(insert_char):
    d = {"{": 0, "(": 0, "[": 0}
    for i in insert_char:
        if i == "{":
            d["{"] += 1
        elif i == "(":
            d["("] += 1
        elif i == "[":
            d["["] += 1
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


print(parentis_validation("(XX)YY{[[(([zzzz}))jjdf]]]"))
print(parentis_validation("()]]]"))
