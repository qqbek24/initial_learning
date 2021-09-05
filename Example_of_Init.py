# ****_example of init
# ****_Autor: Jakub Koziorowski

class Cat:
    def __init__(self,fur_colour="black",number_of_lives=9,number_of_legs=4):
        self.fur_colour = fur_colour
        self.number_of_lives = number_of_lives
        self.number_of_legs = number_of_legs

    def give_sound(self):
        print("miau")

x=Cat()
x.give_sound()
mruczek=Cat()
mruczek.number_of_legs-=1
print(mruczek.number_of_legs)
print(x.number_of_legs)