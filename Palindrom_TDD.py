# ****_Palindrom TDD examples
# ****_Autor: Jakub Koziorowski

class Palindrom:
    def check_validity(self, text):
        if len(text) == 0:
            return False
        if len(text) == 1:
            return True
        text = text.upper()
