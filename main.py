from Domino import Domino

if __name__ == '__main__':
    testDomino = Domino(0, 0)
    testSize = 4

    testDomino.size = 5
    print(testDomino.generate_display_string(2))