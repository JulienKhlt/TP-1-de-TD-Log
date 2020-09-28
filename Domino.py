class Domino :
    def __init__(self, n, m):
        self.n = n
        self.m = m

    # TODO : remplacer par des dictionnaires
    def domino(self, a):
        if (a == 1):
            return [[" "]*5, [" ", " ", "*", " ", " "], [" "]*5]
        elif (a == 2):
            return [["*", " ", " ", " ", " "], [" "]*5, [" ", " ", " ", " ", "*"]]
        elif (a == 3):
            return [["*", " ", " ", " ", " "], [" ", " ", "*", " ", " "], [" ", " ", " ", " ", "*"]]
        elif (a == 4):
            return [["*", " ", " ", " ", "*"], [" "]*5, ["*", " ", " ", " ", "*"]]
        elif (a == 5):
            return [["*", " ", " ", " ", "*"], [" ", " ", "*", " ", " "], ["*", " ", " ", " ", "*"]]
        elif (a == 6):
            return [["*", " ", "*", " ", "*"], [" "]*5, ["*", " ", "*", " ", "*"]]

    def affichage(self):
        L1 = self.domino(self.n)
        L2 = self.domino(self.m)
        print("+-----|-----+")
        for i in range(len(L1)):
            print("|", end="")
            for j in range(len(L1[i])):
                print(L1[i][j], end="")
            print("|", end="")
            for j in range(len(L2[i])):
                print(L2[i][j], end="")
            print("|")
        print("+-----|-----+")
