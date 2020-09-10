# ****_home_work_NoeArk
# ****_Autor: Jakub Koziorowski & Kacper Kalamat

class Worker():

    def __init__(self, wynagrodzenie, okres_zatrudnienia, nazwisko, stanowisko):
        self.wynagrodzenie = wynagrodzenie
        self.okres_zatrudnienia = okres_zatrudnienia
        self.email = nazwisko + "@gmail.com"
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko

    def daj_podwyzke(self):
        if self.okres_zatrudnienia < 5:
            self.wynagrodzenie += 100
        elif self.okres_zatrudnienia>5:
            self.wynagrodzenie += 500

    def awansuj(self):
        tabela_stanowisk = ["junior", "mid", "senior", "manager"]
        for j in range(0, len(tabela_stanowisk)-1):
            if self.stanowisko == tabela_stanowisk[j]:
                self.stanowisko = tabela_stanowisk[j+1]
                print("Awansowales!", self.stanowisko)
                break

    def zwolnij(self):
        self.okres_zatrudnienia = 0
        print("Zostales zwolniony! \nTwój okres zatrudnienia: ", self.okres_zatrudnienia)

firmaX=[]
for x in range(0,1):
    name_txt = str(input("Podaj nazwisko: "))
    #email_txt = str(input("Podaj email: "))
    stanowisko_txt = str(input("Podaj stanowisko (junior, senior, manager): "))
    okresZatrudnienia_txt = float(input("Podaj okres zatrudnienia: "))
    wynagrodzenie_txt = str(input("Podaj wynagrodzenie: "))
    firmaX.append(Worker(wynagrodzenie_txt, okresZatrudnienia_txt, name_txt, stanowisko_txt))

for i in firmaX:
    firmaX[0].awansuj()
    firmaX[0].daj_podwyzke()
    print(firmaX[0].nazwisko)
    print(firmaX[0].wynagrodzenie)
    print(firmaX[0].stanowisko)
    print(firmaX[0].email)
    print(firmaX[0].okres_zatrudnienia)
    firmaX[0].zwolnij()
