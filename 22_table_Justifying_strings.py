# ****_Print formatted table
# ****_Autor: Jakub Koziorowski
def print_table(table):
    """Print table with justifying"""

    for word in table:
        word = str(word)
        print(word.ljust(20), end="")
    print("")


fields = ["name", "email", "feet size"]
person_1 = ["Jan Kowalski", "Ja@gmail.com", 43]
person_2 = ["Kasia Jankowska", "KJanka@gmail.com", 36]
person_3 = ["Pawel_S", "Pawel_Wielka_Stopa@wp.com", 48]

print_table(person_1)
print_table(person_2)
print_table(person_3)
