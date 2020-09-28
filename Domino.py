class Domino :
    def __init__(self, l_value, r_value):
        self.l_value = l_value
        self.r_value = r_value

    def domino(self, value):
        if (value == 0):
            return {}
        elif (value == 1):
            return {(2, 3): "*"}
        elif (value == 2):
            return {(1, 1 ): "*", (3, 5): "*"}
        elif (value == 3):
            return {(1, 1): "*", (2, 3) : "*", (3, 5): "*"}
        elif (value == 4):
            return {(1, 1): "*", (1, 5): "*", (3, 1): "*", (3, 5): "*"}
        elif (value == 5):
            return {(1, 1): "*", (1, 5): "*", (2, 3): "*", (3, 1): "*", (3, 5): "*"}
        elif (value == 6):
            return {(1, 1): "*", (1, 3): "*", (1, 5): "*", (3, 1): "*", (3, 3): "*", (3, 5): "*"}

    # TODO : remplacer par fonction __str__
    def affichage(self):
        Left_domino = self.domino(self.l_value)
        Right_domino = self.domino(self.r_value)
        print("+-----|-----+")
        for i in range(3):
            print("|", end="")
            for j in range(5):
                if (i+1,j+1) in Left_domino:
                    print(Left_domino[(i+1, j+1)], end="")
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