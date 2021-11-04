from typing import List


def generate_grid() -> List[List[str]]:
    import random
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters = []
    grid = []
    for i in range(9):
        letters.append(chr(random.randint(ord('A'), ord('Z'))))
    for i in range(0, (len(letters)), 3):
        stock = []
        stock.append(letters[i])
        stock.append(letters[i+1])
        stock.append(letters[i+2])
        grid.append(stock)
    return grid
# print(generate_grid())

