class Domino :
    def __init__(self, n, m):
        self.n = n
        self.m = m

    # TODO : remplacer par des dictionnaires
    def domino(self, a):
        if ( a==0 ):
            return {}
        elif (a == 1):
            return {(2, 3): "*"}
        elif (a == 2):
            return {(1, 1 ): "*", (3, 5): "*"}
        elif (a == 3):
            return {(1, 1): "*", (2, 3) : "*", (3, 5): "*"}
        elif (a == 4):
            return {(1, 1): "*", (1, 5): "*", (3, 1): "*", (3, 5): "*"}
        elif (a == 5):
            return {(1, 1): "*", (1, 5): "*", (2, 3): "*", (3, 1): "*", (3, 5): "*"}
        elif (a == 6):
            return {(1, 1): "*", (1, 3): "*", (1, 5): "*", (3, 1): "*", (3, 3): "*", (3, 5): "*"}

    def affichage(self):
        L1 = self.domino(self.n)
        L2 = self.domino(self.m)
        print("+-----|-----+")
        for i in range(3):
            print("|", end="")
            for j in range(5):
                if (i+1,j+1) in L1:
                    print(L1[(i+1, j+1)], end="")
                else:
                    print(" ", end="")
            print("|", end="")
            for j in range(5):
                if (i+1, j+1) in L2:
                    print(L2[(i+1, j+1)], end="")
                else:
                    print(" ", end="")
            print("|")
        print("+-----|-----+")
