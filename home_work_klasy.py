# ****_home_work_NoeArk
# ****_Autor: Jakub Koziorowski

class Animals:

    def breath(self):
        print("I am breathing")

    def move(self):
        print("I am moving slowly")

    def eat_food(self):
        print("I am eating")

    def give_a_voice(self):
        print("glos")


class Mammals(Animals):
    def feed_young_with_milk(self):
        print("mlask mlask mlask")


class Insects(Animals):
    def do_not_have_bones(self):
        print("I do not have bones")


class WinglessInsects(Insects):
    pass


class Termits(WinglessInsects):
    def __init__(self, name):
        self.name = name

    def I_eat_wood(self):
        print("I am eating wood")

    def give_a_voice(self):
        print("chrum chrum chrum")


class Giraffes(Mammals):

    def __init__(self, name):
        self.name = name

    def eat_leavs_from_trees(self):
        print("chrup chrup chrup")

    def give_a_voice(self):
        print("Aaaea Aeaaa Aeaaa")


class Monkeys(Mammals):

    def __init__(self, name):
        self.name = name

    def we_can_climb_trees(self):
        print("I am climbing on a tree")

    def give_a_voice(self):
        print("Uuuuaa UUuuaaa UUuaaaa")


class Flying_Groll(Giraffes, Termits):

    def __init__(self, name):
        self.name = name
    # def give_a_voice(self):
        # print("Lubudubu")

# burek = Flying_Groll.eat_leavs_from_trees()


noe_ark = []


for x in range(0, 8):
    if x < 2:
        name_txt = str(input("Write the name of termit: "))
        noe_ark.append(Termits(name_txt))
    elif 2 <= x < 4:
        name_txt = str(input("Write the name of giraffe: "))
        noe_ark.append(Giraffes(name_txt))
    elif 3 < x < 6:
        name_txt = str(input("Write the name of monkey: "))
        noe_ark.append(Monkeys(name_txt))
    elif x >= 6:
        name_txt = str(input("Write the name of Flying_Groll: "))
        noe_ark.append(Flying_Groll(name_txt))

for y in noe_ark:
    print(y.name, " \t", y.give_a_voice(), end="")
    print("\n")
