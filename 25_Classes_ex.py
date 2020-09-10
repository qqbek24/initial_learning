# ****_Classes
# ****_Autor: Jakub Koziorowski

class Animals():
    def breath(self):
        print("I am breathing")
    def move(self):
        print("I am moving slowly")
    def eat_food(self):
        print("I am eating")

class Mammals(Animals):
    def feed_young_with_milk(self):
        print("mlask mlask mlask")

class Giraffes(Mammals):
    def eat_leavs_from_trees(self):
        print("chrup chrup chrup")


burek = Animals()
burek.move()

