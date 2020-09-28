from Domino import Domino
from random import randint

class Game:
    def __init__(self, number_domino):
        self.number_domino = number_domino
        self.victory = False
        self.pioche = [Domino(randint(0, 6), randint(0, 6)) for _ in range(number_domino-7)]
        self.main = [Domino(randint(0, 6), randint(0, 6)) for _ in range(7)]

    def affichage(self):
        for domino in self.main:
            domino.affichage()

    def round(self):
        num_domino = sorted(input("Choisir les numéros des dominos à enlever "), reverse=True)

        somme = 0
        for i in range(len(num_domino)):
            somme += self.main[int(num_domino[i]) - 1].l_value + self.main[int(num_domino[i]) - 1].r_value

        if somme == 12:
            for i in range(len(num_domino)):
                del (self.main[int(num_domino[i]) - 1])
                if len(self.pioche) != 0:
                    domino = self.pioche.pop()
                    self.main.append(domino)
                else:
                    if len(self.main) == 0:
                        self.victory = True
        else:
            print("La somme des points sur les dominos sélectionnés ne fait pas 12. Veuillez réessayer.")

        print(f"Il reste {len(self.pioche)} dominos dans la pioche et {len(self.main)} dans votre main")

    def islost(self):
        pass