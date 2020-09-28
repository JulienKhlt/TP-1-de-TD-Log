from Domino import Domino

if __name__ == '__main__':
    A = Domino(6, 5)
    B = Domino(4, 3)
    C = Domino(2, 1)
    D = Domino(0, 0)

    dominos = [A, B, C, D]

    for domino in dominos:
        domino.affichage()
